# %%

# Fácil - Utilize groupby para somar o número de homicídios por UF no período disponível. Apresente as dez maiores somas e o total nacional acumulado, deixando claro que são contagens absolutas, não taxas. Arquivo: Data/ipea/homicidios.csv

import pandas as pd

df = pd.read_csv('../Data/ipea/homicidios.csv', sep=';')

df.head(3)

# %%

df.groupby(by='período')['valor'].sum()

# %%

df.groupby(by='período')['valor'].sum().sort_values(ascending=False).head(10)

# %%

df.groupby(by='período')['valor'].sum().sort_values(ascending=False).sum()

# %%

# Médio - Agrupe as transações por DescSistemaOrigem e calcule quantidade de transações, total de pontos, média de pontos e amplitude (max - min) com uma função personalizada de agregação. Arquivo: Data/transacoes.csv

import pandas as pd

df = pd.read_csv('../Data/transacoes.csv', sep=';')

df.head(3)

# %%

df.groupby(by='DescSistemaOrigem')['IdTransacao'].count() # Quantidade transacoes por sistema

# %%

df.groupby(by='DescSistemaOrigem')['QtdePontos'].sum() # Quantidade pontos por sistema

# %%

df.groupby(by='DescSistemaOrigem')['QtdePontos'].mean() # Média de pontos por sistema

# %%

def amplitude_pontos(numero: int):
    return (numero.max() - numero.min())

df.groupby(by='DescSistemaOrigem')['QtdePontos'].apply(amplitude_pontos)

# %%

df.groupby(by='DescSistemaOrigem', as_index=False).aggregate({'IdTransacao': ['count'], 'QtdePontos': ['sum', 'mean', amplitude_pontos]})

# %%

# Difícil - Analise as emissões de 2021 por gás e setor econômico. Utilize agrupamento com múltiplos índices, xs, swaplevel e reset_index para identificar, em cada gás, o setor responsável pela maior quantidade emitida. Apresente uma tabela final com gás, setor líder e valor de emissão. Arquivo: Data/database.xlsx — aba GEE Estados

import pandas as pd

df = pd.read_excel('../Data/database.xlsx', sheet_name='GEE Estados')

df.head(3)

# %%

gas_setor = df.groupby(by=['Gás', 'Nível 1 - Setor'])[[2021]].sum()
gas_setor

# %%

gas_setor.xs('CO2 (t)', level='Gás')

# %%

gas_setor.xs('CO2 (t)', level='Gás').idxmax()

# %%

indices = gas_setor.groupby(level='Gás')[2021].idxmax()
indices.to_list()

# %%

lideres = gas_setor.loc[indices]
lideres

# %%

lideres = lideres.reset_index()
lideres

# %%

lideres = lideres.rename(columns={
    'Nível 1 - Setor': 'Setor líder',
    2021: 'Emissão em 2021'
})

lideres # Final do exercicio - Além disso é extra

# %%

lideres = lideres.set_index('Gás')
lideres = lideres['Setor líder']
lideres

# %%

df['Setor líder em emissão'] = df['Gás'].map(lideres)
df

# %%
