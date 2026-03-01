import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sample documents
documents = [
    "AWS provides EC2 virtual servers",
    "S3 is used for object storage in AWS",
    "Machine learning with scikit learn library",
    "Python is used for AI development"
]

# Encode documents
doc_embeddings = model.encode(documents)

# Query
query = "AWS storage service"
query_embedding = model.encode([query])[0]
print(query)
# ---- NumPy Cosine Similarity ----

def cosine_similarity_numpy(query_vec, doc_vecs):
    # Normalize vectors
    query_norm = query_vec / np.linalg.norm(query_vec)
    docs_norm = doc_vecs / np.linalg.norm(doc_vecs, axis=1, keepdims=True)
    
    # Compute similarity
    return np.dot(docs_norm, query_norm)

# Get similarity scores
scores = cosine_similarity_numpy(query_embedding, doc_embeddings)

# Rank documents
ranked_indices = np.argsort(scores)[::-1]

print("Semantic Search Results (NumPy):")
for idx in ranked_indices:
    print(f"Score: {scores[idx]:.4f} | Document: {documents[idx]}")
    