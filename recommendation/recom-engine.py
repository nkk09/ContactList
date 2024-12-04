import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import re

# Load global assets
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
index = faiss.read_index("faiss_index.index")
df = pd.read_csv("processed_dataset.csv")

def extract_fees(prompt):
    """
    Extract budget or fee range from the user's prompt using regex.
    """
    match = re.search(r'\$(\d+)', prompt)
    return int(match.group(1)) if match else None

def search_contacts(prompt, top_k=5):
    """
    Search for contacts matching the user's prompt.

    Args:
        prompt (str): User's query.
        top_k (int): Number of results to return.

    Returns:
        pd.DataFrame: DataFrame with the top matches and their distances.
    """
    # Extract optional fields from the prompt
    max_fees = extract_fees(prompt)
    
    # Generate prompt embedding
    prompt_embedding = model.encode([prompt])

    # Search for the most similar entries
    distances, indices = index.search(prompt_embedding, top_k)
    results = df.iloc[indices[0]].copy()
    results['distance'] = distances[0]
    
    # Filter by fees if specified
    if max_fees is not None:
        results = results[results['Fees'] <= max_fees]
    
    return results


# Test a query
prompt = "Find me a lawyer in New York City under $500"
embedding = model.encode([prompt])
distances, indices = index.search(embedding, 5)

# Display results
results = df.iloc[indices[0]].copy()
results['distance'] = distances[0]
print(results)
