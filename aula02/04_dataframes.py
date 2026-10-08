# %%

import pandas as pd

df_clientes = pd.read_csv('../Data/clientes.csv')

df_clientes.head(10) # Inicio
# %%

df_clientes.tail(10) # Fim
# %%

df_clientes.sample(10) # Amostras aleatórias
# %%

df_clientes.shape # Não é um método, é um atributo. Mostra tamanho de linhas e de colunas
# %%

df_clientes.columns # Mostra todas as colunas (também é um atributo)
# %%

df_clientes.index
# %%

df_clientes.info(memory_usage='deep') # Mostra informações do dataframe, em especial o uso da memória ram
# %%

df_clientes.dtypes # Apresenta uma série mostrando as colunas e seus tipos
# %%

df_clientes.dtypes['qtdePontos'] # Assim podemos ver o tipo de uma coluna específica
# %%

