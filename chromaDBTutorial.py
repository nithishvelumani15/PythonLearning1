import chromadb

client = chromadb.Client()
collection = client.create_collection("policies")
policies = [
    "AWS provides EC2 virtual servers",
    "S3 is used for object storage",
    "Lambda is serverless compute",
    "Chroma is a vector database for AI applications"
]

for i, policy in enumerate(policies):
    collection.add(
        documents=[policy],
        #ids=[f"policy_{i}"]
    )

query = "What is S3?"

result = collection.query(query_texts=query,n_results=2)

print(result.get("documents")[0])