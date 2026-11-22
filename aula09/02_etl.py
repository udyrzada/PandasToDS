# %%

%pip install --upgrade sqlalchemy
%pip install scikit-learn

# %%

import pandas as pd
import sqlalchemy
from sklearn import cluster

with open('etl.sql') as open_file:
    query = open_file.read()

print(query) # Temos o texto da query que foi escrita em outro arquivo

# %%

engine = sqlalchemy.create_engine('sqlite:///../Data/olist.db')

df = pd.read_sql_query(query, con=engine)
df

# %%

kmean = cluster.KMeans(n_clusters=4)
kmean.fit(df[['totalRevenue','qtSales']])

# %%

# Treina modelo de cluster

df['cluster'] = kmean.labels_ # Cria um cluster para cada individuo
df.head()

# %%

# Agora precisamos salvar isso de volta no banco de dados

# O que foi feito com o sklearn foi só para efeito de demonstração, a biblioteca scikit-learn não é abordada no curso

df.to_sql('sellers_cluster', con=engine, index=False, if_exists='replace') # Dessa forma criamos uma tablea nova no banco chamada "sellers_cluster"

# O "if_exists='replace'" se para que se esse script possa ser rodado posteriormente, mesmo existindo uma tabela no banco com o mesmo nome

# %%
