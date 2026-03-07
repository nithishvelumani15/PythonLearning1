import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("policies")

print("Stored vectors:", collection.count())