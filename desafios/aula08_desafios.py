# %%

# Fácil - Faça um merge do tipo left para acrescentar às transações informações de canais dos clientes. Antes da junção, remova duplicidades de identificadores no cadastro. Identifique quantas transações ficaram sem cliente correspondente e valide se a quantidade de linhas foi preservada. Arquivos: Data/transacoes.csv e Data/clientes.csv

import pandas as pd

df_clientes = pd.read_csv('../Data/clientes.csv', sep=';')

df_clientes.head(3)

# %%

df_transacoes = pd.read_csv('../Data/transacoes.csv', sep=';')

df_transacoes.head(3)

# %%

len(df_clientes)

# %%

df_clientes.drop_duplicates(subset='IdCliente', keep='last', inplace=True)
len(df_clientes)

# %%
df_completo = df_transacoes.merge(right=df_clientes, how='left', on='IdCliente', suffixes=['Transacoes',' Clientes'])
df_completo.head(3)

# %%

df_completo['DescSistemaOrigem'].isnull().sum()

# %%

len(df_transacoes) - len(df_completo)

# %%

# Médio - Utilize pd.concat verticalmente para empilhar as bases com uma coluna que identifique o sexo. Depois, filtre o Espírito Santo, ordene ambas as séries por ano e construa uma tabela horizontal com o número de homicídios de homens e mulheres lado a lado, verificando o alinhamento dos períodos. Arquivos: Data/ipea/homicidios-homens.csv e Data/ipea/homicidios-mulheres.csv

import pandas as pd

df_hm = pd.read_csv('../Data/ipea/homicidios-homens.csv', sep=';')

df_hm.head(3)

df_ml = pd.read_csv('../Data/ipea/homicidios-mulheres.csv', sep=';')

df_ml.head(3)

# %%

df_hm['sexo'] = 'H'
df_ml['sexo'] = 'M'

# %%

len(df_ml) + len(df_hm)

# %%

df_full = pd.concat([df_hm, df_ml], axis=0, ignore_index=True)
df_full.head(3)

# %%

len(df_full)

# %%

df_hm_es = df_hm[df_hm['nome'] == 'ES']
df_hm_es.head(3)

# %%

df_hm_es = df_hm_es[['período','valor']].sort_values(by='período')
df_hm_es.rename(columns={'valor': 'homem'}, inplace=True)
df_hm_es.reset_index(drop=True, inplace=True)
df_hm_es.head(3)

# %%

df_ml_es = df_ml[df_ml['nome'] == 'ES']
df_ml_es.head(3)

# %%

df_ml_es = df_ml_es[['período','valor']].sort_values(by='período')
df_ml_es.rename(columns={'valor': 'mulher'}, inplace=True)
df_ml_es.reset_index(drop=True, inplace=True)
df_ml_es.head(3)

# %%

df_hm_es['período'].equals(df_ml_es['período'])

# %%

df_full_es = pd.concat([df_hm_es, df_ml_es['mulher']], axis=1)
df_full_es.head(15)

# %%

# Difícil - Construa uma visão integrada das quatro tabelas, acrescentando a cada item de transação seu cliente, a origem da transação, o nome e a categoria do produto. Calcule ValorItem = QtdeProduto * vlProduto, identifique as cinco categorias com maior valor acumulado e compare os resultados dos sistemas Twitch e Cursos. Arquivos: Data/clientes.csv, Data/transacoes.csv, Data/transacao_produto.csv e Data/produtos.csv

import pandas as pd

transacoes = pd.read_csv('../Data/transacoes.csv', sep=';')
transacoes.head(3)

# %%

clientes = pd.read_csv('../Data/clientes.csv', sep=';')
clientes.rename(columns={'qtdePontos': 'QtdePontos'}, inplace=True)
clientes.head(3)

# %%

transacoes_produto = pd.read_csv('../Data/transacao_produto.csv', sep=';')
transacoes_produto.head(3)

# %%

produtos = pd.read_csv('../Data/produtos.csv', sep=';')
produtos.head(3)

# %%

df_final = transacoes.merge(right=transacoes_produto, how='left', on='IdTransacao', suffixes=['Transacao', 'TransacaoProduto'])

df_final.head(3)

# %%

df_final = df_final.merge(right=produtos, how='left', on='IdProduto')
df_final.head(3)

# %%

df_final = df_final.merge(right=clientes, how='left', on='IdCliente', suffixes=['Transacoes', 'Cliente']).copy()
df_final.head(3)

# %%

df_final['ValorItem'] = df_final['QtdeProduto'] * df_final['vlProduto']
df_final.sample(10)

# %%

df_final.columns
df_final['DescCategoriaProduto'].unique()

# %%

df_final.groupby(by=['DescCategoriaProduto', 'DescSistemaOrigem'])[['ValorItem']].sum().sort_values(by='ValorItem',ascending=False).head().reset_index()

# %%
