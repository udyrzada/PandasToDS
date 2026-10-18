# %%

# Quem teve mais transações de Streak?

import pandas as pd

transacoes = pd.read_csv('../Data/transacoes.csv', sep=';')

transacao_produto = pd.read_csv('../Data/transacao_produto.csv', sep=';')

produtos = pd.read_csv('../Data/produtos.csv', sep=';')

produtos.head(6)

# %%

# Primeiro passo é vincular o id do cliente com o id do produto

cliente_transacao_produto = transacoes.merge(transacao_produto, how='left', on='IdTransacao')

cliente_transacao_produto = cliente_transacao_produto[['IdTransacao', 'IdCliente', 'IdProduto']]

cliente_transacao_produto.head()

# %%

df_full = cliente_transacao_produto.merge(produtos, how='left', on='IdProduto')

df_full.head(3)

# %%

# Filtrar só para pegar Streak

df_full = df_full[df_full['DescNomeProduto'] == 'Presença Streak']

# Pegar o maior valor

df_full.groupby('IdCliente')['IdTransacao'].count().max()
df_full.groupby('IdCliente')['IdTransacao'].count().idxmax()

# ou

df_full.groupby('IdCliente')['IdTransacao'].count().sort_values(ascending=False).head(1)

# %%

# Forma mais "avançada" de se fazer

produtos = produtos[produtos['DescNomeProduto'] == 'Presença Streak']

(
    transacoes.merge(transacao_produto, on="IdTransacao", how="left")
    .merge(produtos, on="IdProduto", how="right") # Poderia ser inner também
    .groupby(by="IdCliente")["IdTransacao"]
    .count()
    .sort_values(ascending=False)
    .head(1)
)

# Dessa forma empilhamos os comandos sem precisar ficar reatribuindo

# %%
