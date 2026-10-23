# %%

# Fácil - Importe o arquivo, examine suas dimensões, colunas, tipos e consumo de memória. Exiba as primeiras e últimas linhas e construa uma visão contendo somente identificador, nome e categoria. Arquivo: Data/produtos.csv

import pandas as pd

df = pd.read_csv('../Data/produtos.csv', sep=';')
df

# %%

df.shape

# %%

df.columns

# %%

df.dtypes

# %%

df.info(memory_usage='deep')

# %%

df.head()

# %%

df.tail()

# %%

df_2 = df[['IdProduto', 'DescNomeProduto', 'DescCategoriaProduto']]
df_2

# %%

# Médio - Importe o cadastro, renomeie qtdePontos para PontosCliente, escolha cinco colunas relevantes e reorganize sua ordem. Exporte o resultado para um novo CSV e reimporte o arquivo para verificar se a estrutura foi preservada. Arquivo: Data/clientes.csv

import pandas as pd

df = pd.read_csv('../Data/clientes.csv', sep=';')
df.head()

# %%

df = df.rename(columns={'qtdePontos': 'pontosClientes'})

df.head()

# %%

colunas = df.columns.to_list()
colunas.sort()
colunas

# %%

df = df[colunas]
df

# %%

df.to_csv('DataDesafios/clientes_atividade.csv', index=False)

# %%

df = pd.read_csv('../Data/clientes_atividade.csv')
df.head(3)

# %%

# Difícil - Faça uma inspeção independente das duas bases, comparando dimensões, consumo de memória, tipos de dados e amostras. Crie duas visões simplificadas e exporte uma para CSV e outra para Excel. Arquivos: Data/transacoes.csv e Data/UFs.csv

transacoes = pd.read_csv('../Data/transacoes.csv', sep=';')

transacoes.head(3)

# %%

ufs = pd.read_csv('../Data/UFs.csv')

ufs.head(3)

# %%

transacoes.shape

# %%

ufs.shape

# %%

transacoes.info(memory_usage='deep')

# %%

ufs.info(memory_usage='deep')

# %%

transacoes.dtypes

# %%

ufs.dtypes

# %%

transacoes_simplificado = transacoes[['IdTransacao', 'IdCliente', 'QtdePontos']]
transacoes_simplificado.head()

# %%

transacoes_simplificado.to_csv('DataDesafios/transacoes_simplificado.csv', index=False)

# %%

ufs_simplificado = ufs[['Unidade federativa', 'Abreviação', 'PIB (2015)']]
ufs_simplificado.head()

# %%

ufs_simplificado.to_excel('DataDesafios/ufs_simplificado.xlsx', index=False)

# %%
