from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
import faiss

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')  # A small, efficient embedding model

# Load your dataset
df = pd.read_csv(r"C:/Users/admin/OneDrive - American University of Beirut/Desktop/ContactList/recom-engine/cleaned_people_dataset.csv")
print(df.head())  # Preview your data

# Combine relevant fields into one text representation
df['combined'] = (
    df['First Name'] + " " + df['Last Name'] + ", " +  # Name
    df['Job Title'] + " in " + df['City'] + ", " + df['Country'] + ". " +
    "Fees: $" + df['Fees'].astype(str)  # Fees
)

# Generate embeddings for each entry
embeddings = model.encode(df['combined'].tolist(), show_progress_bar=True)

# Save embeddings for later use
np.save("embeddings.npy", embeddings)  # Save as a .npy file
df.to_csv("processed_dataset.csv", index=False)  # Save processed dataset

# Load embeddings if you've saved them
embeddings = np.load("embeddings.npy").astype('float32')

# Build FAISS index
dimension = embeddings.shape[1]  # Embedding dimensions
index = faiss.IndexFlatL2(dimension)  # L2 distance for similarity
index.add(embeddings)  # Add embeddings to the index

faiss.write_index(index, "faiss_index.index")  # Save the index file

print(f"Index contains {index.ntotal} entries.")  # Verify