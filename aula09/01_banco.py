# %%

%pip install --upgrade sqlalchemy

# %%

import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

clientes = pd.read_sql_table(table_name='tb_customers', con=engine)

# %%

clientes.head()

# %%

# Não é uma boa prática lermos a tabela inteira de uma vez. Empresas grandes recebem milhões de transações novas todos os dias. Fica impraticável puxar todas as informações de uma tabela desse tamanho. Nem o Python, nem a rede aguentam.

# Pra resolvermos isso, podemos executar uma query

query = "SELECT * FROM tb_customers LIMIT 100"

df_100 = pd.read_sql_query(query, con=engine)
df_100

# Com as querys, podemos fazer consultas no banco utiliando SQL da forma que quisermos

# %%

