# %%

import pandas as pd

idades = [19, 20, 35, 23, 32, 43, 28]

series_idades = pd.Series(idades)
series_idades
# %%

print(idades[0])
print(series_idades[0])

print(idades[-1])

# %%

print(series_idades[-1])

# %%

print(series_idades[6])
# %%

series_idades = series_idades.sort_values()
series_idades

# O index no pandas fica vinculado à linha da série, como um ID (como um campo/valor de um dicionário).

# Mesmo que ordenando a serie, o indice permanece o mesmo, algo que não aconteceria em uma lista.

# %%

series_idades.iloc()

print(series_idades)
print(series_idades.iloc()[-1])

# Utilizando o método 'iloc()', podemos utilizar o index como posição, e não mais como chave.

# %%

print(series_idades.iloc()[:3])

# Assim pegamos os 3 primeiros elementos como em uma lista.

# %%

idades = [19, 20, 35, 23, 32, 43, 28]

indexs = ["Udir", "Arthur", "Ana", "Marcos", "Lucas", "Jão", "Lucas"]

series_idades = pd.Series(idades, index=indexs)
series_idades

# Assim definimos o index da primeira lista, como o nome referente na segunda lista.

# %%

series_idades.iloc[0]

# Mas mesmo assim podemos buscar como posição, independente do index ser ou não numérico.

# %%

series_idades["Lucas"]

# Retorna todos os valores com o indice = "Lucas".

# %%

series_idades.iloc[[-1]]

# Como usamos [[-1]], o resultado continua sendo uma Series, e não apenas um valor isolado. 

# Sem utilizar o 'iloc' estamos navegando pelos indices, utilizando o 'iloc' navegamos pelas linhas.
