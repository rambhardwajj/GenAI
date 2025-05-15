import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()
client = genai.Client()


# List of analogy prompts
analogies = [
    "Paris is to France as Rome is to ?",
    "Bird is to Fly as Fish is to ?",
    "Hot is to Cold as Day is to ?",
    "King is to Queen as Man is to ?",
    "Eyes are to See as Ears are to ?"
]

print("\n🔁 Analogy Solver Results:\n")

for prompt in analogies:
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=prompt
    )
    print(f"🧠 {prompt} → {response.text.strip()}")
