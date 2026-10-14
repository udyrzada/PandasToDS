# Criando colunas novas a partir de colunas que já existem

# %%

import pandas as pd
import numpy as np # É o pai do Pandas

df = pd.read_csv('../Data/clientes.csv', sep=';')

df.head()
# %%

df['pontos_100'] = df['qtdePontos'] + 100

# Somando 100 a cada valor em qtdePontos

# %%

df.head()
# %%

df['email_ou_twitch'] = df['flEmail'] | df['flTwitch']
df.head(10)

# Cria uma nova coluna que mostra se tem email ou twitch

# %%

# Quantas redes socias a pessoa tem cadastrada?

redes = ['flEmail', 'flTwitch', 'flYouTube', 'flBlueSky', 'flInstagram']

df['qtdeRedesSociais'] = df[redes].sum(axis=1) # O axis=1 indica que a soma será realizada horizontalmente, ou seja, entre as colunas de cada linha.

# Ou pode fazer também  df['aoMenosUmaRedeSocial'] = df['flEmail'] |	df['flTwitch'] | df['flYouTube'] | df['flBlueSky'] | df['flInstagram']

df.head(10)
# %%

df['aoMenosUmaRedeSocial'] = df['flEmail'] |	df['flTwitch'] | df['flYouTube'] | df['flBlueSky'] | df['flInstagram']

# Ou pode fazer também --> df['aoMenosUmaRedeSocial'] = df[redes].any(axis=1)

df.head(10)

# %%

df['qtdePontos'].describe() # Muita assimetria

# %%

df['logPontos'] = np.log1p(df['qtdePontos']) # Ou np.log(df['qtdePontos']+1)

# O NumPy aplica o logaritmo natural a cada valor da coluna, reduzindo a escala dos dados e evitando problemas com valores iguais a zero.

# %%

df['logPontos'].describe() # Muito mais simétrico. Tudo isso por causa da utilização do numpy (log nesse caso)

# %%

import matplotlib.pyplot as plt
plt.hist(df['qtdePontos'])
plt.grid(True)
plt.show

# %%

plt.hist(df['logPontos'])
plt.grid(True)
plt.show

# Se parece muito mais com uma distribuição normal que a anterior (não significa que seja, de fato, uma distribuição normal)

# %%
