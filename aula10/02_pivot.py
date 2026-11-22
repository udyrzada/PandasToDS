# %%

import pandas as pd

df = pd.read_csv('../Data/homicidios_consolidado.csv', sep=';')

df.head()

# %%

df = df.set_index(['nome', 'período'])
df_stack = df.stack()
df_stack

# %%

df_stack = df_stack.reset_index()
df_stack.columns = ['nome', 'período', 'métricas', 'valor']
df_stack

# %%

df_pivot = df_stack.pivot_table(values='valor', index=['nome', 'período'], columns='métricas')
df_pivot

# O pivot não é simplesmente uma alternativa ao unstack. Ele serve para modelar o dataframe da maneira que preferir, definindo valores, index e colunas

# %%

df_pivot.reset_index()

# %%

df_stack.pivot_table(values='valor', index='nome', columns='métricas', aggfunc='mean')

# Dessa forma utilizamos a média dos valores em vez de utilizar o período, através da função de agregação (aggfunc)

# %%
