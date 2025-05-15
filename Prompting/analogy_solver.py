import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env
load_dotenv()
client = genai.Client()


# List of analogy prompts
analogies = [
    "Paris is to France as Rome is to ?",
]

print("\n Analogy Solver Results:\n")

for prompt in analogies:
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=prompt
    )
    print(f" {prompt} → {response.text.strip()}")


print("\n Enter your own analogies below!")
inp = ''
while True:
    user_input = input("\nEnter an analogy or 'q' to quit: ")
    if user_input.lower() == 'q':
        print("Chalo bye!")
        break
    inp = inp + user_input + "\n"
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=inp
    )
    print(f" {user_input} → {response.text.strip()}")