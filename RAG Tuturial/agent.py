from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import chromadb
from sentence_transformers import SentenceTransformer
from documentRetriver import file_content
load_dotenv()

client = chromadb.Client()
embed_model = SentenceTransformer('BAAI/bge-small-en-v1.5')
#embed_model = SentenceTransformer('all-MiniLM-L6-v2')
collection = client.create_collection("policies")
policies = file_content()
policy_embeddings = embed_model.encode(policies).tolist()

collection.add(
    documents=policies,
    embeddings=policy_embeddings,
    ids=[f"policy_{i}" for i in range(len(policies))]
)
    
class HR_Assistant:
    def __init__(self,user_prompt, HR_Policies):
        self.user_prompt = user_prompt
        self.HR_Policies = HR_Policies
        self.My_key = os.getenv("GeminiAPIKey")
        self.client = genai.Client(api_key=self.My_key)
    def askAi(self):
        try:
            context_text = "\n".join(self.HR_Policies)
            full_prompt = f""" Assume yoursellf as an HR Assistant.
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

prompt1 = HR_Assistant(user_query, result["documents"][0])
prompt1.askAi()
