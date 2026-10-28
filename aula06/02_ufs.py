# %%

import pandas as pd

uf = pd.read_csv('../Data/UFs.csv', sep =',')

uf.head()
# %%

uf.dtypes

# %%

# Transformando um numero para float

numero = '164 122,2'

numero = float(numero.replace(' ', '').replace(',', '.'))

# %%

# Agora podemos fazer uma função para isso

def str_to_float(numero:str):
    return float(numero.replace(' ', '').replace(',', '.').replace("\xa0", '')) #  O \xa é um caso especial do HTML

# %%

uf['Área (km²)'] = uf['Área (km²)'].apply(str_to_float)

uf

# %%

uf.dtypes

# %%

uf['PIB per capita (R$) (2015)'] = uf['PIB per capita (R$) (2015)'].apply(str_to_float)

# %%

uf.info()
# %%

def mortalidade_to_float(numero:str):
    return (float(numero.replace(' ', '').replace(',', '.').replace('‰', '')) / 1000)

uf['Mortalidade infantil (2016)'] = uf['Mortalidade infantil (2016)'].apply(mortalidade_to_float)

# %%

uf.info()
# %%

# Se o PIB / Capita for maior do que 30.000 e a mortalidade for menor que 15/1000 e o IDH for maior que 700, retorne "Parece bom", caso contrário retorna "Não parece bom"

linha = uf.iloc[0]
linha

# %%

(linha['PIB per capita (R$) (2015)'] > 30000 and linha['IDH (2010)'] > 700 and linha['Mortalidade infantil (2016)'] < 0.015)

# Essa é uma forma de fazer varias comparações de um dataframe só que utilizando uma series. Porque quando utilizamos o iloc, retorna uma series daquela linha específica

# %%

def parece_bom(linha:pd.Series):
    if (linha['PIB per capita (R$) (2015)'] > 30000 and linha['IDH (2010)'] > 700 and linha['Mortalidade infantil (2016)'] < 0.015):
        return 'Parece bom'
    else:
        return 'Não parece bom'

# %%

uf['Bom ou não'] = uf.apply(parece_bom, axis=1) # Axis = 1 --> Linha | Axis = 0 --> Coluna
uf
# %%
