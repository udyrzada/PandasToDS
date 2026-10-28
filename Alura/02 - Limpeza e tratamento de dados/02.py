# %%

import pandas as pd
import json

with open('../Data/dados.json') as f:
    json_bruto = json.load(f)

df = pd.json_normalize(json_bruto, record_path='pessoas')
df.head(3)

# %%

df.info()

# %%

df = df.explode('telefones')
df

# %%

df['idade'] = df['idade'].astype(int)
df.info()

# %%

df['nome'] = df['nome'].replace('[^a-zA-Z0-9À-ÿ\-\']', '', regex=True).str.title()
df['endereco.cidade'] = df['endereco.cidade'].replace('[^a-zA-Z0-9À-ÿ ]', '', regex=True).str.title()
df

# %%
