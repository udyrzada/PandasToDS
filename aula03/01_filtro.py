# %%

import pandas as pd

# %%

pessoas = pd.DataFrame({
    "nome": ['Arthur', 'Ana', 'João'],
    "idade": [22, 22, 10],
    "uf": ['ES', 'ES', 'SP']
})

filtro_idade = pessoas['idade'] >= 18

pessoas[filtro_idade] # O filtro é uma serie, que contem a mesma quantidade de elementos de linhas no meu DF

# %%


df = pd.read_csv('../Data/transacoes.csv', sep=';')
df.head()
filtro = (df['QtdePontos'] >= 50) & (df['QtdePontos'] <= 100)
df[filtro] # Filtrando para mostrar apenas quando a linha possui uma QtdePontos maior do que 50
# %%
