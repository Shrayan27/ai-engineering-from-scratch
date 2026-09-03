import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ["GROQ_API_KEY"]
)

MODEL = os.environ.get("LLM_MODEL", "llama-3.1-8b-instant")

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": "What is a neural network in one sentence?"
        }
    ],
)

print(response.choices[0].message.content)
