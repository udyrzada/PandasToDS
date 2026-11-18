# %%

import pandas as pd

df = pd.read_csv('../Data/homicidios_consolidado.csv', sep=';')
df.head()

# %%

# A ideia aqui é empilhar todas as colunas em apenas 2, que vão o conter o valor "Métrica" e "Valor". Ou seja, nosso dataframe vai crescer verticalmente e diminuir horizontalmente

# Porque isso é importante de saber? Porque quando as métricas estão em colunas, caso uma nova métrica surja, todo o dataframe terá que ser mudado. Mais fácil mudar o número de linhas do que mudar o número de colunas

df = df.set_index(['nome', 'período'])
df

# %%

df_stack = df.stack() # Ele transforma o dataframe em uma serie
df_stack

# %%

# Para ver em formato de dataframe

df_stack = df_stack.reset_index()
df_stack.columns = ['nome', 'período', 'métrica',' valor']
df_stack

# %%

# Agora como fazer a volta disso (desempilhar a tabela)? Utilizamos o unstack

df = df_stack.set_index(['nome', 'período', 'métrica']).unstack() # O segredo está na definição do index
df

# %%

df = df.reset_index()

# %%

df.columns # Está como multi-index, precisamos resolver isso

# %%

metricas = df.columns.droplevel(0)[2:].to_list()
df.columns = ['nome', 'período'] + metricas
df

# %%
