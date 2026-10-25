# %%

# Fácil - Converta DtCriacao e DtAtualizacao para datetime. Extraia o ano e o mês da criação, conte datas ausentes e compare os tipos das colunas antes e depois. Arquivo: Data/clientes.csv

import pandas as pd

df = pd.read_csv('../Data/clientes.csv', sep=';')

df.head(3)

# %%

df['DtCriacao'] = pd.to_datetime(df['DtCriacao'])
df['DtAtualizacao'] = pd.to_datetime(df['DtAtualizacao'])

df.dtypes

# %%

df.dropna(subset='DtCriacao', axis=0, inplace=True)
df['MesEAno'] = (df['DtCriacao'].dt.month).astype(str) + '/' + (df['DtCriacao'].dt.year).astype(str)

# Ou: df['MesEAno'] = df['DtCriacao'].dt.strftime('%m/%Y')

df

# %%

df[['DtCriacao', 'MesEAno']]

# %%

# Médio - Identifique registros incompletos nas colunas homicidios e homicidios-mulheres. Crie uma base comparável contendo somente observações válidas para ambas as métricas e informe quantas linhas foram excluídas. Arquivo: Data/homicios_consolidado.csv

import pandas as pd

df = pd.read_csv('../Data/homicidios_consolidado.csv', sep=';')

df.head()

# %%

tamanho_antigo = df.shape

# %%

df.dropna(subset=['homicidios', 'homicidios-mulheres'], how='any', inplace=True)
df.reset_index(inplace=True, drop=True)

# %%

tamanho_novo = df.shape

# %%

print(f'Antigo: {tamanho_antigo} | Novo: {tamanho_novo}')

# %%

# Difícil - Construa um cadastro com no máximo uma linha por IdCliente. Trate dados ausentes, converta datas e utilize sort_values e drop_duplicates para priorizar registros completos e, quando necessário, os mais recentemente atualizados. Exporte clientes_tratados.csv e apresente uma auditoria das exclusões. Arquivo: Data/clientes.csv

import pandas as pd

df = pd.read_csv('../Data/clientes.csv', sep=';')

df.head(3)

# %%

df['qtdePontos'] = df['qtdePontos'].fillna(0)
df

# %%

df = df.dropna()
df[['DtCriacao', 'DtAtualizacao']] = df[['DtCriacao', 'DtAtualizacao']].apply(pd.to_datetime)
df.dtypes

# %%

df.shape

# %%

df = df.drop_duplicates(subset='IdCliente', keep='last')

df.shape

# %%

df.sort_values(by='DtAtualizacao', ascending=False, inplace=True)
df.reset_index(inplace=True, drop=True)
df.head(3)

# %%

df.to_csv('DataDesafios/clientes_tratados.csv', sep=';')

# %%
