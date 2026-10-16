# Selecione a primeira transação diária de cada cliente

# %%

import pandas as pd

df = pd.read_csv('../Data/transacoes.csv', sep=';')

df.head()
# %%


df['DtCriacao'] = pd.to_datetime(df['DtCriacao'])
df['DtCriacaoDate'] = df['DtCriacao'].dt.date

df = df.sort_values(by='DtCriacao')

df

# %%

df = df.drop_duplicates(subset=['IdCliente', 'DtCriacaoDate'], keep='first')

df
# %%