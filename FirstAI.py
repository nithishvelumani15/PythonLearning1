from google import genai
from google.genai import types
import os
import asyncio
from dotenv import load_dotenv
from pathlib import Path
from google.adk.agents import LlmAgent

load_dotenv()

class CodeVerifier:
    def __init__(self):
        self.My_key = os.getenv("GeminiAPIKey")
        self.code_verifier = LlmAgent(
                name="Code_Verifier_Agent",
                model="gemini-2.5-flash",
                description="An agent who helps to verify the code written by the developer",
                instruction="""Assume yourself as a professional software engineer. 
                                You are receiving a programming file.
                                Analyze the code for secrity bugs, potental issues. Give suggestions to improve.
                                Keep the output more simple and in a friendly tone. Your output should be understandable
                                even for a beginner. Output should be under specifc topics like Security issues and 
                                under the heading output should be in pointers in seperate line """
            )
    def askAi(self):
        try:
            response = self.code_verifier.run()
            print(f"Response from Gemini: {response.text}")
            """
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=self.user_prompt,
                config= types.GenerateContentConfig(
                system_instruction=", If you found issues in the code try to give a corrected code by yourself. Do not use Markdown formatting (no asterisks, bolding, or headers). Provide plain text only."
                )
            )
            """            
        except Exception as e:
            print(f"An error occurred: {e}")
"""
folder = Path(r"C:\Users\nithi\Desktop\My Projects\Sample Folder")
for file in folder.iterdir():
    with open(file, "r") as f:
        file_content = f.read()
        file_name = file.name
"""
prompt1 = CodeVerifier()
prompt1.askAi()
