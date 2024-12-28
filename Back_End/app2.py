import os
from dotenv import load_dotenv

from flask import Flask, request, jsonify
from flask_cors import CORS

from langchain.chains import LLMChain
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import SystemMessage
from langchain.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Groq API configuration
groq_api_key = os.environ.get("API_KEY")
model = "llama3-8b-8192"

client = ChatGroq(groq_api_key=groq_api_key, model_name=model)

# System prompt and memory configuration
system_prompt = """You are a highly experienced and professional doctor with 
                   exceptional expertise in patient care and communication. Your responses should reflect
                    a deep understanding of medical science while maintaining a compassionate, patient-centric approach. 
                    Use clear, precise language to convey information, ensuring that complex medical
                    oncepts are simplified without losing accuracy. Your tone should be warm, empathetic,
                      and reassuring, instilling confidence and comfort in the patient. When providing advice,
                      consider the patient's concerns holistically, addressing not just the symptoms but also
                      their emotional well-being. Strive to make every interaction feel like a thoughtful
                        and thorough consultation, fostering trust and a positive experience.
            """
conversational_memory_length = 5

memory = ConversationBufferWindowMemory(
    k=conversational_memory_length, memory_key="chat_history", return_messages=True
)


def get_response(text):
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{human_input}"),
        ]
    )
    conversation = LLMChain(
        llm=client,
        prompt=prompt,
        verbose=False,
        memory=memory,
    )
    response = conversation.predict(human_input=text)
    return response


@app.route("/response", methods=["POST"])
def response():
    try:
        data = request.get_json()
        query = data.get("query")
        if not query:
            return jsonify({"error": "Query parameter is missing"}), 400
        chatbot_response = get_response(query)
        return jsonify({"response": chatbot_response}), 200
    except Exception as e:
        app.logger.error(f"Error: {e}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
