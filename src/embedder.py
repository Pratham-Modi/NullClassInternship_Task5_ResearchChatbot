import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm
import os

def load_data(csv_path):
    df = pd.read_csv(csv_path, dtype={0: str})
    df['text'] = df['title'].fillna('') + ". " + df['abstract'].fillna('')
    return df

def generate_embeddings(texts):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = []
    for text in tqdm(texts, desc="Generating embeddings"):
        emb = model.encode(text)
        embeddings.append(emb)
    return np.array(embeddings)

def save_embeddings(embeddings, output_path): 
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    np.save(output_path, embeddings)
    print(f"Embeddings saved to: {output_path}")

if __name__ == "__main__":
    csv_path = "data/arxiv_subset.csv"
    output_path = "models/paper_embeddings.npy"

    df = load_data(csv_path)
    texts = df['text'].tolist()

    embeddings = generate_embeddings(texts)
    save_embeddings(embeddings, output_path)
