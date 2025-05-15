from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model = 'gemini-2.0-flash-001', 
    contents='Hello there!',
    config=types.GenerateContentConfig(
        temperature=1.1,
        max_output_tokens=50
    )
)
print(response.text)
