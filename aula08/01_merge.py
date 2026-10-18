# %%

import pandas as pd

transacoes = pd.read_csv('../Data/transacoes.csv', sep=';')

transacoes.head(3)

clientes = pd.read_csv('../Data/clientes.csv', sep=';')

clientes.head(3)

# Agora iremos trabalhar com mais de uma base de dados ao mesmo tempo

# %%

transacoes.merge(right=clientes, how='left', on='IdCliente', suffixes=['Transacao', 'Cliente'])

# O merge() é utilizado para unir dois dataframes, e funciona como um JOIN do SQL

# 'right' --> Define o segundo DataFrame
# 'how' --> Define o tipo de junção: mantém todas as linhas de transacoes, mesmo que não exista um cliente correspondente (podendo ser left, right, inner ou outer)
# 'on' --> Define a coluna utilizada para relacionar os dois DataFrames. Essa coluna deve existir em ambos. Como se fosse uma "chave estrangeira"
# 'suffixes' --> Define o sufixo caso existam colunas com mesmos nomes, porém em dataframes diferentes

# %%

# Exemplo para chaves não correspondentes

df_1 = pd.DataFrame({
    'transacao': [1,2,3,4,5],
    'idCliente': [1,2,3,2,2],
    'valor': [10,45,32,17,87]
    })

df_2 = pd.DataFrame({
    'id': [1,2,3,4],
    'nome': ['Arthur', 'Ana', 'Luiza',' Pedro']
    })

# Como cruzar o df_1 com df_2?

# %%

df_1.merge(df_2, left_on=['idCliente'], right_on='id', how='inner')

# Para especificar as colunas utilizamos 'left_on' e 'right_on', como forma de linkar chave e valor

# %%
