from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

class CodeVerifier:
    def __init__(self,user_prompt):
        self.user_prompt = user_prompt
        self.My_key = os.getenv("GeminiAPIKey")
        self.client = genai.Client(api_key=self.My_key)
    def askAi(self):
        try:
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=self.user_prompt,
                config= types.GenerateContentConfig(
                system_instruction="Do not use Markdown formatting (no asterisks, bolding, or headers). Provide plain text only."
                )
            )
            print(f"Gemini: {response.text}")
            
        except Exception as e:
            print(f"An error occurred: {e}")

userquestion = input("Enter you question: ")
prompt1 = CodeVerifier(userquestion)
prompt1.askAi()