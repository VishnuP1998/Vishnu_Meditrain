import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("API_KEY"),
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": """You are a highly experienced and professional doctor with 
                   exceptional expertise in patient care and communication. Your responses should reflect
                    a deep understanding of medical science while maintaining a compassionate, patient-centric approach. 
                    Use clear, precise language to convey information, ensuring that complex medical
                    oncepts are simplified without losing accuracy. Your tone should be warm, empathetic,
                      and reassuring, instilling confidence and comfort in the patient. When providing advice,
                      consider the patient's concerns holistically, addressing not just the symptoms but also
                      their emotional well-being. Strive to make every interaction feel like a thoughtful
                        and thorough consultation, fostering trust and a positive experience.
            """,
        },
        {
            "role": "user",
            "content": "Having regular headahce",
        },
    ],
    model="llama3-8b-8192",
)

# print(chat_completion.choices[0].message.content)
print(chat_completion)


#  Generate Responses -> Create API (flask) -> UI (React / HTML+Css)