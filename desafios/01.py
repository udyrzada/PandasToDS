"""
1 - Encontre os valores únicos das colunas "Nível 1 - Setor" e "Estado" para identificar as atividades econômicas presentes na base de dados e se todos os Estados do Brasil estão presentes no DataFrame.

2 - Filtre o DataFrame somente com os dados dos Estados da região Sul do Brasil.

3 - Filtre o DataFrame para exibir apenas os registros em que o campo "Nível 1 - Setor" seja igual a "Mudança de Uso da Terra e Floresta" e o campo "Estado" seja igual a "AM" (sigla para o Estado do Amazonas).

4 - Encontre o valor máximo de emissão do ano de 2021 para os dados de "Agropecuária" no Estado do Pará.
"""

# %%

import pandas as pd
%pip install openpyxl

# %%

df = pd.read_excel('../Data/database.xlsx', sheet_name='GEE Estados')
df.head()

# %%

# 1 - Encontre os valores únicos das colunas "Nível 1 - Setor" e "Estado" para identificar as atividades econômicas presentes na base de dados e se todos os Estados do Brasil estão presentes no DataFrame.

nivel1_setor = df['Nível 1 - Setor'].unique()
nivel1_setor

# %%
estados = df['Estado'].unique()
estados
# %%

# 2 - Filtre o DataFrame somente com os dados dos Estados da região Sul do Brasil.

sul = ['PR', 'SC', 'RS']

filtro = df['Estado'].isin(sul)
# %%

df[filtro]
# %%

# 3 - Filtre o DataFrame para exibir apenas os registros em que o campo "Nível 1 - Setor" seja igual a "Mudança de Uso da Terra e Floresta" e o campo "Estado" seja igual a "AM" (sigla para o Estado do Amazonas).

filtro = (df['Estado'] == 'AM') & (df['Nível 1 - Setor'] == 'Mudança de Uso da Terra e Floresta')
df[filtro].head()
# %%

# 4 - Encontre o valor máximo de emissão do ano de 2021 para os dados de "Agropecuária" no Estado do Pará.

df
# %%

filtro = (df['Nível 1 - Setor'] == 'Agropecuária') & (df['Estado'] == 'PA')
df[filtro][2021].max()

# Outra forma: emissoes_gases.loc[(emissoes_gases['Nível 1 - Setor'] == 'Agropecuária') & (emissoes_gases['Estado'] == 'PA'), 2021].max()

# %%

df = df.drop(columns='Nível 2')

# %%

df.head()
# %%
