# %%

import pandas as pd

df = pd.DataFrame({
    "cliente": [1, 2, 3, 4, 5],
    "nome": ["teo", "jose", "nah", "mah", "lah"],
})

df_02 = pd.DataFrame({
    "cliente": [6, 7, 8],
    "nome": ["kozato", "laura", "dan"],
    "idade": [32, 29, 31]
})

df_03 = pd.DataFrame({
    'idade': [32, 34, 19, 54, 33]
})

# %%

# O concat espera receber uma LISTA de DATAFRAMES

pd.concat([df, df_02]) # Ele empilha e concatena os dataframes

# %%

pd.concat([df, df_02], ignore_index=True) # Dessa forma ele ignora o indice antigo

# %%

pd.concat([df, df_03]) # É empilhado de uma forma que não gostariámos

# %%

# Para corrigir isso, podemos passar um parâmetro específico

pd.concat([df, df_03], axis=1) # Com o axis podemos alterar se queremos concatenar de cima para baixo ou da esquerda para direita

# %%

df_03 = df_03.sort_values(by='idade')

pd.concat([df, df_03], axis=1) # Mesmo ordenando pela idade, o DataFrame final continua da mesma forma (ele segue os indices para ordenar)

# %%

# Para resolver isso, precisamos fazer um reset_index:

df_03 = df_03.sort_values(by='idade').reset_index(drop=True)
df_03

# %%

pd.concat([df, df_03], axis=1) 

# %%

