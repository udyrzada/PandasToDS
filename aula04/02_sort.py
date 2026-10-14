# %%

import pandas as pd

clientes = pd.read_csv('../Data/clientes.csv', sep=';')

clientes.head(10)
# %%

clientes['qtdePontos'].sort_values() # Ordena por quem tem mais pontos

# Os indices foram 'embaralhados' no processo

# %%

clientes['qtdePontos'].sort_values().tail(5) # Pegando os 5 maiores valores unicos

# Porém, dessa forma ordena apenas uma série, não o dataframe inteiro

# %%

clientes.sort_values(by='qtdePontos')

# Dessa forma ordena todo o dataframe, a partir de uma serie, passando essa serie como critério

# %%

clientes.sort_values(by='qtdePontos', ascending=False)

# Ordena de forma decrescente
# %%

clientes.sort_values(by='qtdePontos', ascending=False).head(5) # Pega os 5 maiores (agora no dataframe inteiro)
# %%

# Como faço para pegar apenas o ID dos 5 maiores valores?

clientes.sort_values(by='qtdePontos', ascending=False).head(5)['idCliente']
# %%

# Como podemos ordenar um dataframe com base em 2 critérios?

exemplo = pd.DataFrame({
    'nome': ['João', 'Pedro', 'Davi'],
    'idades': [20, 30, 45],
    'salario': [2500, 2500, 1000]
})

exemplo.sort_values(by=['salario', 'idades'], ascending=[False, True])

# Utilizando listas podemos utilizar mais de um critério, inclusive cada um podendo ter ordenações distintas
# %%
