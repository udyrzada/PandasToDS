# %%



df = pd.read_csv('../Data/transacao_produto.csv', sep=';')
df.head()
# %%

filtro = (df['IdProduto'] == '5') | (df['IdProduto'] == '11')
df[filtro]
# %%

filtro = df['IdProduto'].isin(['5', '11']) # Forma de criar um filtro com base em valores específicos de uma coluna

df[filtro]
# %%

import pandas as pd

df_clientes = pd.read_csv('../data/clientes.csv', sep=';')

filtro = df_clientes['DtCriacao'].notnull() # Forma de criar um filtro com apenas as datas que não sejam nulas
df_clientes[filtro]
# %%

# Negando uma afirmação (basta colocar um '~' na frente)

filtro = ~df_clientes['DtCriacao'].notnull() # Agora mostra apenas as datas nulas
df_clientes[filtro]
# %%
