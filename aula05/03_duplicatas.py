# %% 

import pandas as pd

# %% 

df = pd.DataFrame({
    'nome': ['Arthur', 'Ana Luiza', 'Lucas', 'Ana Luiza', 'Lucas'],
    'sobrenome': ['Sandrini', 'Godinho', 'Sartorato', 'Godinho', 'Sartorato']

})

df

# %%

df.drop_duplicates(keep='last') # Remove linhas duplicadas (mantenho o ultimo valor adicionado)

# %%


df = pd.DataFrame({
    'nome': ['Arthur', 'Ana Luiza', 'Lucas', 'Ana Luiza', 'Lucas'],
    'sobrenome': ['Sandrini', 'Godinho', 'Sartorato', 'Godinho', 'Sartorato'],
    'salario': [2000, 3000, 4000, 5000, 6000]

})

df

df.drop_duplicates(keep='last') # Agora não funciona pq não tem linhas COMPLETAMENTE repetidas

# %%

# Forma de resolver isso:

df.drop_duplicates(subset=['nome', 'sobrenome']) # Mantém o primeiro pq "keep='last'" não foi declarado

# %%

# Se eu quiser manter o de maior salário, antes de fazer o drop_duplicates eu tenho que ordenar por salário:

df = pd.DataFrame({
    'nome': ['Arthur', 'Ana Luiza', 'Lucas', 'Ana Luiza', 'Lucas'],
    'sobrenome': ['Sandrini', 'Godinho', 'Sartorato', 'Godinho', 'Sartorato'],
    'salario': [2000, 3000, 4000, 5000, 6000]

})

df = df.sort_values(by='salario', ascending=False)

df

df.drop_duplicates(subset=['nome', 'sobrenome'])

# %%
