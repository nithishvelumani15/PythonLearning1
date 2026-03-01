from google.adk.agents import LlmAgent
import os
from dotenv import load_dotenv
from google.adk.knowledge import Knowledge, LocalFolder

load_dotenv()


code_assistant  = LlmAgent(
    name="Code_Verifier_Agent",
    model="gemini-2.5-flash",
    description="An agent who verifies developer code",
    instruction="""
You are a professional software engineer.
You will receive a programming file of any laguage. The user will paste the code as plain text.

Analyze it for:

1. Security Issues
2. Code Improvements

Keep explanation beginner friendly.
Use bullet points under each heading.
"""
)
root_agent = code_assistant