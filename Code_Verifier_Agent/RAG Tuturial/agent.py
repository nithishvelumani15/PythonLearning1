from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import chromadb
from sentence_transformers import SentenceTransformer

load_dotenv()

client = chromadb.Client()
embed_model = SentenceTransformer('BAAI/bge-small-en-v1.5')
collection = client.create_collection("policies")
policies = [
    "All full-time employees are entitled to 20 days of Paid Time Off (PTO) per calendar year, accrued at 1.67 days per month.",
    "PTO carryover is limited to 5 days, which must be utilized within the first quarter of the following year.",
    "Employees are granted 10 days of paid sick leave annually for personal illness or family care.",
    "A formal medical certificate is mandatory for any sick leave exceeding three consecutive business days.",
    "Maternity leave provides 16 weeks of fully paid leave for employees with at least 12 months of continuous service.",
    "Paternity leave provides 2 weeks of paid leave to be taken within the first 12 weeks of a child's birth or adoption.",
    "The hybrid work policy requires employees to be physically present in the office a minimum of 3 days per week.",
    "Employees are eligible for a one-time home-office reimbursement of up to $500 for ergonomic equipment.",
    "All employees must complete the mandatory Annual Ethics and Anti-Bribery training within 30 days of their start date.",
    "Secondary employment or external business interests must be disclosed to and approved by HR to avoid conflicts of interest.",
    "The company maintains a zero-tolerance policy regarding workplace harassment, discrimination, or bullying.",
    "All company-issued hardware, including laptops and mobile devices, must remain encrypted and password-protected.",
    "Unauthorized installation of third-party software on company devices is strictly prohibited for security reasons.",
    "The standard resignation notice period is 30 days for individual contributors and 60 days for management roles.",
    "Final settlement, including prorated PTO payouts, will be processed within 15 days of the employee's last working day.",
    "New hires are subject to a 90-day probationary period, during which performance is reviewed monthly."
]
policy_embeddings = embed_model.encode(policies).tolist()

collection.add(
    documents=policies,
    embeddings=policy_embeddings,
    ids=[f"policy_{i}" for i in range(len(policies))]
)
    
class CodeVerifier:
    def __init__(self,user_prompt, HR_Policies):
        self.user_prompt = user_prompt
        self.HR_Policies = HR_Policies
        self.My_key = os.getenv("GeminiAPIKey")
        self.client = genai.Client(api_key=self.My_key)
    def askAi(self):
        try:
            context_text = "\n".join(self.HR_Policies)
            full_prompt = f"""
            Answer strictly using the context below.
            If the answer is not available in the context, say:
            "Please reach out to your respective HR."
            Context: {context_text}
            Question:{self.user_prompt}
            """
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=full_prompt,
                config= types.GenerateContentConfig(
                system_instruction="Do not use Markdown formatting (no asterisks, bolding, or headers). " \
                "Provide plain text only."
                )
            )
            print(f"Gemini: {response.text}")
            
        except Exception as e:
            print(f"An error occurred: {e}")

user_query = input("Enter you question: ")
query_vec = embed_model.encode([user_query]).tolist()
result = collection.query(query_embeddings=query_vec,n_results=10)

prompt1 = CodeVerifier(user_query, result["documents"][0])
prompt1.askAi()