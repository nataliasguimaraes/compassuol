import pandas as pd
import json

df = pd.read_csv('movies.csv', encoding='utf-8', sep='|', low_memory=False)

df['anoLancamento'] = pd.to_datetime(df['anoLancamento'], format='%Y', errors='coerce')
df = df.dropna(subset=['anoLancamento'])

df_filtered = df.loc[(df['anoLancamento'].dt.year >= 2000) & (df['genero'].isin(['Romance', 'Drama']))]

filtered_ids = list(set(df_filtered['id'].tolist()))

print(filtered_ids)

data = {"ids": filtered_ids}

with open('movies_filtered.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
