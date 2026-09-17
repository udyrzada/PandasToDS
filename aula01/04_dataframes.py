# %%

import pandas as pd

idades = [19, 20, 35, 23, 32, 43, 28]

nomes = ["Udir", "Arthur", "Ana", "Marcos", "Lucas", "Jão", "Lucas"]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# Um dataframe é um varal onde pode-se 'pendurar' as series.

# %%

df = pd.DataFrame()
df['idades'] = series_idades
df['nomes'] = series_nomes

df

# Um dataframe é um CONJUNTO de series. Enquanto series são linhas, um dataframe é composto por linhas e colunas (matriz).

# %%

df['nomes']
df.loc[-1]

# %%

df.sort_values(by='nomes')
df.loc[0]

# Com o 'loc' navegamos por linhas, diferente do 'iloc' que navegamos por indices.

# %%

df.iloc[-1]['nomes']

# Dessa forma podemos pegar o campo específico da ultima posição da tabela.

# %%
