# %%

import pandas as pd

df = pd.read_csv('../Data/clientes.csv', sep=';')

df.head()

# %%

# O apply serve para aplicar uma função em uma serie, elemento a elemento, sem precisar declarar um loop manualmente

def get_last_id(id_cliente):
    return id_cliente.split('-')[-1] # Pega a ultima parte o id somente

df['idCliente'].apply(get_last_id)

# %%

