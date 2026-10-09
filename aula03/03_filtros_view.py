# Filtros não são cópias

# %%

import pandas as pd

df = pd.read_csv('../Data/clientes.csv', sep=';')

df.head()
# %%

filtro = df['qtdePontos'] == 0
df[filtro]

clientes_0 = df[filtro]

# Clientes_0 não está criando uma copia de df, ele está apenas apontando para as linhas de df, mas apontando apenas para as linhas onde a condição é verdadeira

# O beneficio disso é que não duplica o banco (duplicar ia gerar o dopro de gasto de memoria), ele apenas cria uma variável apontando para linhas específicas

clientes_0['flag_1'] = 1

clientes_0

# %%

# Para mudar essa condição, basta utilizar o .copy()

clientes_0 = df[filtro].copy()

clientes_0['flag_1'] = 1

clientes_0

# %%
