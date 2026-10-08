# %%

import pandas as pd
# %%

series = pd.Series([1, 2, 3, 4, 5])
# %%

# Como importar arquivos que estão fora do ambiente do Python

df = pd.read_csv('../Data/clientes.csv', sep=';')
df
# %%

# Salvando o arquivo

df.to_csv('../Data/clientes.csv', index=False)
# %%

# Salvando como arquivo Parquet (arquivo binário)

df.to_parquet('../Data/clientes.parquet', index=False)
# %%

# Salvando como Excel

df.to_excel('../Data/clientes.xlsx', index=False)
# %%
