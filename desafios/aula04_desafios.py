# %%

# Fácil - Crie PontosComBonus, adicionando 100 pontos a cada cliente, e EmailOuTwitch, identificando quem possui pelo menos um dos dois canais ativos. Arquivo: Data/clientes.csv

import pandas as pd

df = pd.read_csv('../Data/clientes.csv', sep=';')

df.head(3)

# %%

df['qtdePontos'] = df['qtdePontos'].fillna(0)

df['PontosComBouns'] = df['qtdePontos'] + 100
df.head(3)

# %%

filtro = (df['flEmail'] == 1) | (df['flTwitch'] == 1)

df['EmailOuTwitch'] = filtro
df.head(10)
# %%

# Médio - Calcule quantas redes sociais cada cliente possui, utilizando sum(axis=1), e crie uma flag indicando se possui alguma rede. Produza um ranking dos 15 primeiros, ordenando pela quantidade de redes e, em caso de empate, pelos pontos. Arquivo: Data/clientes.csv

import pandas as pd

df = pd.read_csv('../Data/clientes.csv', sep=';')

df.head(3)

# %%

redes = ['flEmail', 'flTwitch', 'flYouTube', 'flBlueSky', 'flInstagram']

df['QuantidadeRedes'] = df[redes].sum(axis=1)
df.head(10)

# %%

filtro = df['QuantidadeRedes'] != 0

df['PossuiRede'] = filtro
df.head(10)

# %%

df.sort_values(by=['QuantidadeRedes', 'qtdePontos'], ascending=False).head(15)

# %%

# Difícil - Crie uma versão válida da base para aplicar np.log1p aos pontos, excluindo valores negativos e ausentes. Compare as estatísticas descritivas e crie dois histogramas: antes e depois da transformação logarítmica. Arquivo: Data/clientes.csv

import pandas as pd
import numpy as np 

df = pd.read_csv('../Data/clientes.csv', sep=';')

df.head(3)

# %%

df.describe()

# %%

df.dropna(subset=['qtdePontos'], inplace=True)
df = df[df['qtdePontos'] > 0]

df.head(10)

# %%

df.describe()

# %%

df['logPontos'] = np.log1p(df['qtdePontos'])
df.describe()

# %%

%pip install matplotlib

# %%

df[['qtdePontos', 'logPontos']].hist(figsize=(10, 3))

# %%
