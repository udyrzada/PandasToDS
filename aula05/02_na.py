# %%

import pandas as pd

clientes = pd.read_csv('../Data/clientes.csv', sep=';')

# %%

clientes.head(4)

# %%

# A primeira opção para lidar com NAs é removendo eles 

clientes.dropna() # Apaga todas as linhas que tenham pelo menos 1 NA

# Isso é uma view, ou seja, para as mudanças ficarem salvas, é necessario atribuir novamente ao dataframe. Ex: clientes = clientes.dropna() 

# %%

clientes.dropna(how='all') # Agora o critério para fazer o drop é que toda a linha seja NA. O default para how é 'any'

# %%

clientes.dropna(subset=['DtCriacao']) # Com o subset é possível remover utilizando um critério. No exemplo, utilizamos a coluna 'DtCriacao', onde se ela se encontrar com NA, a linha sera apagada

# %%

clientes.dropna(subset=['DtCriacao', 'DtAtualizacao'], how='all') # Podemos misturar os dois critérios agora. Onde só vai ser excluida a linha se ambas as colunas passadas forem NA (por causa do how='all')

# %%

clientes.fillna(0) # Aqui em vez de apagar a linha que tenha NA eu estou substituindo por um valor (neste caso é 0). É uma INPUTAÇÃO de dados
# %%

clientes.fillna({'Cliente': 'alguem', 'qtdePontos': 0}) # Posso criar um dicionário para atribuir valores diferentes para cada coluna

# %%

media = clientes['qtdePontos'].mean()
clientes['qtdePontos'].fillna(media) # Aqui estou substituindo o NA da coluna qtdePontos pela média da própria coluna

# %%

