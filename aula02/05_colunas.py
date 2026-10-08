# %%

import pandas as pd

df = pd.read_csv('../Data/transacoes.csv', sep=';')
# %%

df.shape
# %%

df.info(memory_usage='deep')
# %%

df.dtypes
# %%

df = df.rename(columns={'DtCriacao': 'DataCriacao'}) # Renomeando uma coluna de um DataFrame (precisa salvar em uma variável, se não a mudança fica apenas na memória)
# %%

df
# %%

df.rename(columns={'QtdePontos': 'QtPontos'}, inplace=True) # Mudando dessa forma (utilizando o inplace=True) não precisa atribuir novamente o dataframe na variável
# %%

df
# %%

df['IdCliente'] # Acessando uma coluna específica (em forma de SERIE)
# %%

df[['IdCliente', 'QtPontos']] # Acessando mais de uma coluna (em forma de DATAFRAME)
# %%

# SELECT * FROM df

df
# %%

# SELECT IdCliente FROM df

df[['IdCliente']]
# %%

# SELECT IdCliente, QtPontos FROM df LIMIT 5

df[['IdCliente', 'QtPontos']].head(5)
# %%

# SELECT IdCliente, IdTransacao, QtPontos FROM df LIMIT 5

df[['IdCliente', 'IdTransacao', 'QtPontos']].head(5)
# %%

# Como reordenar as colunas do DataFrame

colunas = df.columns.tolist()
colunas.sort()
df = df[colunas]

df

# Reordenando em ordem alfabética
# %%
