import os
import json
import urllib.request
import urllib.error

from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

# Groq API endpoint
url = "https://api.groq.com/openai/v1/chat/completions"

# Request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['GROQ_API_KEY']}",
    "User-Agent": "Mozilla/5.0",
}

# Request body
body = json.dumps({
    "model": os.environ.get("LLM_MODEL", "openai/gpt-oss-20b"),
    "messages": [
        {
            "role": "user",
            "content": "What is a neural network in one sentence?"
        }
    ],
}).encode("utf-8")

# Create POST request
req = urllib.request.Request(
    url,
    data=body,
    headers=headers,
    method="POST",
)

# Send request and read response
try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode("utf-8"))

        print(
            result["choices"][0]["message"]["content"]
        )

except urllib.error.HTTPError as error:
    print(f"HTTP Error: {error.code}")
    print(error.read().decode("utf-8"))
