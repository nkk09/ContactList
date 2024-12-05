from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
import faiss
from pathlib import Path

model = SentenceTransformer('all-MiniLM-L6-v2')

current_dir = Path(__file__).parent.parent
cleaned_data_path = current_dir /"data" / "raw" / "cleaned_people_dataset.csv"
processed_data_path = current_dir/"data"/"processed"/"processed_dataset.csv"
embeddings_data_path = current_dir/"recommendation"/"faiss_index"/"embeddings.npy"
faiss_data_path = current_dir/"recommendation"/"faiss_index"/"faiss_index.index"

df = pd.read_csv(cleaned_data_path)
df.columns = df.columns.str.replace(' ', '_').str.lower()
df['combined'] = (
    df['first_name'] + " " + df['last_name'] + ", " +
    df['job_title'] + " in " + df['city'] + ", " + df['country'] + ". " +
    "Fees: $" + df['fees'].astype(str)
)

# Generate embeddings for each entry
embeddings = model.encode(df['combined'].tolist(), show_progress_bar=True)
np.save(str(embeddings_data_path), embeddings)
df.to_csv(str(processed_data_path), index=False)
embeddings = np.load(str(embeddings_data_path)).astype('float32')

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)
faiss.write_index(index, str(faiss_data_path))

# Verify eno 1000 entries
print(f"Index contains {index.ntotal} entries.")