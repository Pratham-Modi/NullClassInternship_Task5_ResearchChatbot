import json
import pandas as pd
import os

# === INPUT FILE ===
input_path = 'data/arxiv-metadata-oai-snapshot.json'

# === OUTPUT FILE ===
output_path = 'data/arxiv_subset.csv'

# === Create a list to store filtered papers ===
cs_papers = []

print("⏳ Processing arXiv dataset...")

# === Open the large JSON file line by line ===
with open(input_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            paper = json.loads(line)
            # Filter only Computer Science papers
            if paper.get('categories', '').startswith('cs.'):
                cs_papers.append({
                    'id': paper.get('id'),
                    'title': paper.get('title'),
                    'authors': paper.get('authors'),
                    'abstract': paper.get('abstract'),
                    'categories': paper.get('categories'),
                    'update_date': paper.get('update_date')
                })
        except json.JSONDecodeError:
            continue  # Skip bad lines

print(f"✅ Found {len(cs_papers)} Computer Science papers")

# === Save to CSV ===
df = pd.DataFrame(cs_papers)
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)
print(f"✅ Saved to {output_path}")
