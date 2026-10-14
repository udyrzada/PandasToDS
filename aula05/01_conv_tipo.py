# %%

import pandas as pd

df = pd.read_csv('../Data/clientes.csv', sep=';')
df.head()

# %%

df['qtdePontos'].astype(float) 
df['qtdePontos'] = df['qtdePontos'].astype(float) # Convertendo de int para float

df['qtdePontos']

# %%

# O replace serve para substituirmos valores que não são desejados

df['DtCriacao'] = df['DtCriacao'].replace({'0000-00-00 00:00:00.000': '2000-01-01 01:00:00.000'}) # Substitui utilizando 'chave: valor'

# %%

df['DtCriacao'] = pd.to_datetime(df['DtCriacao']) # Convertendo String para Datetime


# %%

df['DtCriacao'].dt.year # Pode-se utilizar o dt em colunas que sejam do tipo datetime para acessar atribuitos específicos, como dia, ano, mês, hora, etc...

# %%
