import os
from dotenv import load_dotenv
from groq import Groq

import requests
from flask import Flask, request, jsonify

from flask_cors import CORS

load_dotenv()

app = Flask(__name__)

CORS(app)

client = Groq(
    api_key=os.environ.get("API_KEY"),
)


def get_reponse(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """You are a highly experienced and professional doctor with 
            exceptional expertise in patient care and communication. Your responses should reflect
              a deep understanding of medical science while maintaining a compassionate, patient-centric approach. 
              Use clear, precise language to convey information, ensuring that complex medical
                concepts are simplified without losing accuracy. Your tone should be warm, empathetic,
                  and reassuring, instilling confidence and comfort in the patient. When providing advice,
                    consider the patient's concerns holistically, addressing not just the symptoms but also
                      their emotional well-being. Strive to make every interaction feel like a thoughtful
                        and thorough consultation, fostering trust and a positive experience.
                """,
            },
            {
                "role": "user",
                "content": text,
            },
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content


@app.route("/", methods=["GET"])
def checkHealth():
    try:
        return jsonify({"status": "Health check ok"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/response", methods=["POST"])
def response():
    try:
        data = request.get_json()
        query = data.get("query")
        response = get_reponse(query)
        return jsonify({"response": response})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


def get_users():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    return response.json()


@app.route("/test_users", methods=["GET"])
def test_users():
    try:
        response = get_users()
        users = response["data"]["data"]
        return jsonify(users)

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
