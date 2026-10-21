# %%

# Fácil - Utilizando cinco valores reais de homicídios de 1989, crie manualmente uma Series com as siglas dos estados como índices. Calcule média, variância, mínimo e máximo. Identifique o estado com maior número de registros. Arquivo: Data/ipea/homicidios.csv

import pandas as pd

valores_homicidios = [100, 200, 300, 400, 500]
ufs = ['ES', 'SP', 'RJ', 'MG', 'BA']

series = pd.Series(valores_homicidios, index=ufs)
series

series.mean()
series.min()
series.max()
series.var()

series.max()

series.sort_values().iloc()[[-1]]

# %%

# Médio - Crie uma Series com seis quantidades reais de pontos, utilizando rótulos personalizados. Ordene-a de forma decrescente e compare o acesso a elementos por rótulo com o acesso por posição usando iloc. Arquivo: Data/clientes.csv

import pandas as pd

index = ['Arthur', 'João', 'Pedro', 'Ana', 'Luis', 'Arthur']

series = pd.Series([10, 50, 10, 30, 1, 0], index=index)

series

# %%

series = series.sort_values(ascending=False)
series

# %%

series.loc['Arthur']

# %%

series.iloc[-1]

series.iloc[[-1]]

# %%

# Difícil - Com os seis primeiros produtos, construa manualmente duas Series, uma para nomes e outra para categorias. Combine-as em um DataFrame, ordene os produtos alfabeticamente e demonstre acessos por loc e iloc. Arquivo: Data/produtos.csv

import pandas as pd

nomes = ['Mouse', 'Teclado', 'Mesa', 'Travesseiro', 'Camisa', 'Tênis']

categorias = ['Periféricos', 'Periféricos', 'Móveis', 'Quarto', 'Roupas', 'Calçados']

nomes = pd.Series(nomes)
categorias = pd.Series(categorias)

nomes
categorias

# %%

df = pd.DataFrame({
    'produtos': nomes,
    'categoria': categorias})

df

# %%

df = df.sort_values(by='produtos')
df

# %%

df.loc[0]

# %%

df.iloc[0]

# %%
