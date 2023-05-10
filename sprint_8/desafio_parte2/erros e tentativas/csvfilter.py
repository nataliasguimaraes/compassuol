import pandas as pd
import json

df = pd.read_csv('movies.csv', encoding='utf-8', sep='|', low_memory=False)

df_filtered = df[df['genero'].isin(['Romance'])]

filtered_ids = df_filtered['id'].tolist()

print(filtered_ids)

data = {"ids": filtered_ids}

with open('filmes_filtered.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
