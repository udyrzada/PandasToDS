# %%

import pandas as pd

transacoes = pd.read_csv('../Data/transacoes.csv', sep=';')

transacoes.head(3)

# %%

transacoes.groupby(by='IdCliente')['QtdePontos'].sum()

# %%

transacoes.groupby(by='IdCliente').count()

# %%

transacoes.groupby(by='IdCliente', as_index=False)[['IdTransacao']].count()

# Exibindo em forma de dataframe

# %%

transacoes.groupby(by='IdCliente')['IdTransacao'].count()

# Exibindo em forma de serie

# %%

# Quero: Quantidade de transacoes, total de pontos e pontos/transacao

summary = transacoes.groupby(by='IdCliente', as_index=False).aggregate({'IdTransacao': ['count'], 'QtdePontos': ['sum', 'mean']})

# O aggregate (ou agg) serve para fazer atribuições a mais de uma coluna ao mesmo tempo

summary # Isso é um dataframe multi-index. Porque a coluna QtdePontos, por exemplo, agora é dividida em 'sum' e em 'mean'

summary['QtdePontos'] # Retorna outro dataframe em vez de retornar uma serie

# Formas de acessar a serie:

summary['QtdePontos']['mean']

# ou

summary[('QtdePontos', 'mean')]

# %%

# Podemos mudar essa estrutura hierarquica, apenas atribuindo novos nomes as colunas

summary.columns

summary.columns = ['IdCliente', 'IdTransacao', 'PontosTotal', 'MédiaPontos']

summary

# %%

