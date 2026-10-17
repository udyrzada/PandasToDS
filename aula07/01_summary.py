# %%

import pandas as pd

idades = [32, 55, 34, 20, 19, 78, 40]

idades = pd.Series(idades)
idades

# %%

# Tipos de agregação

idades.sum()
idades.min()
idades.max()
idades.mean()

idades.describe() # É uma lista de estatísticas

# %%

clientes = pd.read_csv('../Data/clientes.csv', sep=';')

clientes.head(3)

# %%

clientes['flTwitch'].sum() # Quantidade de seguidores na twitch

clientes['flTwitch'].mean() # Porcentagem de quantos seguem na twitch (tbm é a média)

# %%

redes_sociais = ['flEmail',	'flTwitch',	'flYouTube',	'flBlueSky',	'flInstagram']

clientes[redes_sociais].mean() # É possível aplicar em dataframes também

# %%

clientes.mean(numeric_only=True)

# %%

lista_numericos = clientes.dtypes[~(clientes.dtypes == 'str')].index.to_list()

clientes[lista_numericos].describe() 

# É necessário fazer isso pois o método describe não possui o 'numeric_only'

# %%
