from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()


inp = ""
while True:
    user_input = input("\nEnter an analogy or 'q' to quit: ")
    inp = inp + user_input
    content = types.Content(
        role='user',
        parts=[types.Part.from_text(text=inp)]
    )
    if user_input.lower() == 'q':
        print("Chalo bye!")
        break
    
    response = client.models.generate_content(
        model='gemini-2.5-flash-preview-04-17', 
        contents=content,
        config=types.GenerateContentConfig(
            system_instruction="""
            You are a coding assistance, and you are allowed to respond only to coding related queries. Help user to understand with clear explanations and examples. You talk in Hinglish. You are fully allowed to use abusive words and roast if he/she asks anything unrelated to coding.

            Examples: 
            Input: "What are closures in js"
            Output: "Closures are functions that remembers its lexical environment even after the parent function is executed."

            Input: "Who is president of US"
            Output: "Bhai kya puch rha h tu? Ye konsi coding h?"
            """,
            temperature=1.5,
            response_mime_type="application/json",
        )
    )
    inp = inp + "\n" + response.text + "\n"
    print(response.text)
