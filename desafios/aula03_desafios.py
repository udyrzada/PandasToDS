# %%

# Fácil - Encontre todas as transações com QtdePontos entre 50 e 100, inclusive. Exiba os identificadores e a quantidade de pontos das primeiras ocorrências e informe quantas transações atendem ao critério. Arquivo: Data/transacoes.csv

import pandas as pd

df = pd.read_csv('../Data/transacoes.csv', sep=';')
df.head(3)

# %%

filtro = (df['QtdePontos'] >= 50) & (df['QtdePontos'] <= 100)
df[filtro].head()

# %%

df[filtro].count()

# %%

# Médio - Selecione transações de produtos com códigos '5' ou '11' e quantidade igual a 1. Compare resultados obtidos com operadores booleanos e isin, crie uma cópia independente e informe a quantidade de ocorrências de cada código. Arquivo: Data/transacao_produto.csv

import pandas as pd

df = pd.read_csv('../Data/transacao_produto.csv', sep=';')
df.head(3)

# %%

filtro = df['IdProduto'].isin(['5', '11']) & (df['QtdeProduto'] == 1)

df[filtro].head()

# %%

df = df[filtro]
df

# %%

df.count()

# %%

# Difícil - Identifique clientes que possuam pelo menos um dos canais Email, Twitch ou YouTube habilitado, tenham 100 pontos ou mais e possuam data de criação preenchida. Apresente o total elegível e os 20 clientes com mais pontos, preservando o DataFrame original. Arquivo: Data/clientes.csv

import pandas as pd

df = pd.read_csv('../Data/clientes.csv', sep=';')
df.head()

# %%

lista_colunas = ['flEmail', 'flTwitch', 'flYouTube']

filtro = ((df[lista_colunas] != 0).any(axis=1)) & (df['qtdePontos'] >= 100) & (df['DtCriacao'].isnull() == False)
df[filtro].sort_values(by='qtdePontos', ascending=False).head(20)

# %%