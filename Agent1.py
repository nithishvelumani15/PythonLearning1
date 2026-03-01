from google.adk.agents import LlmAgent
import os
from dotenv import load_dotenv

load_dotenv()

agent = LlmAgent(
    name="Code_Verifier_Agent",
    model="gemini-2.5-flash",
    description="An agent who verifies developer code",
    instruction="""
You are a professional software engineer.
You will receive a Python file.
Analyze it for:

1. Security Issues
2. Code Improvements
3. Best Practices

Keep explanation beginner friendly.
Use bullet points under each heading.
"""
)