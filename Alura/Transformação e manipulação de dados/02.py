# %%

import pandas as pd

df = pd.read_json('../Data/moveis_disponiveis.json')

df.head(3)

# %%

df['data'] = pd.to_datetime(df['data'])
df.head(3)

# %%

df.info()

# %%

df['anoMes'] = df['data'].dt.strftime('%Y/%m')

# %%

df.groupby(by='anoMes')['vaga_disponivel'].sum()

# %%
