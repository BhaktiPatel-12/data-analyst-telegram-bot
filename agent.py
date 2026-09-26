import os
import json

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_question(question):

    prompt = f"""
You are an expert data analyst.

Solve the user question.

Rules:
- Return ONLY JSON.
- No markdown.
- No explanations.
- Match exactly the JSON structure requested by the user.

User question:

{question}
"""


    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )


    output = response.choices[0].message.content.strip()


    try:
        return json.loads(output)

    except:

        return {
            "raw_answer": output
        }