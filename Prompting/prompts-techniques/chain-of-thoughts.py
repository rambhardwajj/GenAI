import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()

client = genai.Client()

system_prompt = """
You are an AI assistant who is expert in breaking down complex problems and then resolve the user query.

For the given user input, analyse the input and break down the problem step by step.
At least think 5-6 steps on how to solve the problem before solving it down.

The steps are: "analyse", then "think" (repeated), then "output", then "validate", and finally "result".

Rules:
1. Follow the strict JSON output as per Output schema.
2. Carefully analyse the user query.
3. Always respond with an array of JSON objects like:
[
  {"step": "analyse", "content": "..."},
  {"step": "think", "content": "..."},
  ...
]
"""

while True:
    user_input = input("\nEnter a problem (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break

    content = types.Content(
        role="user",
        parts=[types.Part.from_text(text=user_input)]
    )
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash-preview-04-17',
            contents=content,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=1,
                response_mime_type="application/json"
            )
        )

        # Parse JSON array of steps
        steps = json.loads(response.text)
        print(steps)

        print("\n🧠 Reasoning Steps:")
        for step in steps:
            label = step.get("step", "").title()
            content = step.get("content", "")
            print(f"{label}: {content}")

    except Exception as e:
        print("❌ Error:", e)
