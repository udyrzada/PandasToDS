# %%

# Objetivo geral ---> Deixar a base de dados limpa e tratada para treinar o modelo de ML

import pandas as pd

df = pd.read_json('../Data/dataset-telecon.json')

df.head(3)

# %%

df['conta'][0] # Os valores estão no formato chave:valor

# %%

pd.json_normalize(df['conta']).head(3)

# %%

pd.json_normalize(df['telefone']).head(3)

# %%

import json

with open('../Data/dataset-telecon.json') as f:
    json_bruto = json.load(f)
    # Maneira 1 de normalizar dados json
json_bruto

# %%

df = pd.json_normalize(json_bruto)
df.head(3)

# %%

data = {
  "nome": "João",
  "idade": 28,
  "enderecos": [
    {
      "tipo": "casa",
      "rua": "Rua A",
      "numero": 123,
      "cidade": "São Paulo"
    },
    {
      "tipo": "trabalho",
      "rua": "Rua B",
      "numero": 456,
      "cidade": "Rio de Janeiro"
    }
  ]
}

df = pd.json_normalize(data,  record_path='enderecos', meta=['nome', 'idade']) 

# Maneira 2 de normalizar dados json

df.head(3)

# %%

