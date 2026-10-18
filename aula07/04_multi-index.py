# %%

import pandas as pd
%pip install openpyxl

df = pd.read_excel('../Data/database.xlsx', sheet_name='GEE Estados')

df.head(3)

# %%

# Podemos agrupar por mais de uma coluna

gas_setor = df.groupby(['Gás', 'Nível 1 - Setor'])[[2021]].sum() # Para utilizar o multi-index, não devemos utilizar o 'as_index=False'. Pois cada coluna do groupby será um index novo

gas_setor

# Embora visualmente pareça uma tabela com três colunas, Nível 1 - Setor e Gás são índices, e apenas 2021 é uma coluna de dados (2021 está duplamente associada a cada um dos indices)

# %%

# Método cross-section

gas_setor.xs('CO2 (t)', level=0) # Level 1 do indice (Nível 1 - setor)

gas_setor.xs('CO2 (t)', level=0).max() # Para achar o maior valor

gas_setor.xs('CO2 (t)', level=0).idxmax() # Para achar o index de onde está o maior valor

