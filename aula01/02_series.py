# %%

idades = [19, 20, 35, 23, 32, 43, 28]

media = sum(idades) / len(idades)

n = len(idades)

soma = 0

for i in idades:
    soma += (i - media) ** 2

variancia = soma / (len(idades) - 1)

print(f"Media:{media}")
print(f"Variancia: {variancia}")

# %%

import pandas as pd

series_idades = pd.Series(idades)
series_idades

# %%

media_idades = series_idades.mean()
media_idades
variancia_idades = series_idades.var()
variancia_idades
summary_idades = series_idades.describe()
summary_idades

# %%
