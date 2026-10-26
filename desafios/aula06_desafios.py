# %%

# Fácil - Desenvolva uma função para extrair somente o último bloco de um UUID, após o último hífen. Aplique-a aos identificadores dos clientes e crie uma nova coluna. Arquivo: Data/clientes.csv

import pandas as pd

df = pd.read_csv('../Data/clientes.csv', sep=';')

df.head(3)

# %%

string_teste = '000dc0f6-e4f2-4a42-b8cd-b586ed1c709a'

def separa_id (id: str):
    return id.split('-')[-1]

print(separa_id(string_teste))

# %%

df['IdClienteFinal'] = df['IdCliente'].apply(separa_id)
df

# %%

# Médio - Crie uma função para converter textos numéricos com espaços e vírgulas decimais em valores float. Utilize-a nas colunas de área territorial e PIB per capita. Mostre os novos tipos e as cinco maiores áreas. Arquivo: Data/UFs.csv

import pandas as pd

df = pd.read_csv('../Data/UFs.csv')

df.head(3)

# %%

string_teste = '164 122,2  '

def trata_to_float(numero: str):
    return float(numero.replace(',', '.').replace(' ', '').replace('\xa0', '').strip())

print(trata_to_float(string_teste))

# %%

colunas_to_float = ['Área (km²)', 'PIB (2015)']

df[colunas_to_float] = df[colunas_to_float].map(trata_to_float)
df

# %%

df[['Área (km²)', 'PIB (2015)']].sort_values(by='Área (km²)', ascending=False).head(5)

# %%

# Difícil - Converta população, área e mortalidade infantil para números. Calcule a densidade populacional de 2022 e crie uma função aplicada por linha que classifique como Prioritário os estados com densidade acima de 100 habitantes/km² e mortalidade infantil superior a 15 por mil. Arquivo: Data/UFs.csv

import pandas as pd

df = pd.read_csv('../Data/UFs.csv')

df.head(3)

# %%

def trata_to_float(numero: str):
    return float(numero.replace(',', '.').replace(' ', '').replace('\xa0', '').replace('‰', '').strip())

colunas_to_float = ['População (Censo 2022)', 'Área (km²)', 'Mortalidade infantil (2016)']

df[colunas_to_float] = df[colunas_to_float].map(trata_to_float)
df

# %%

def calc_densidade (linha: pd.Series):
    return (linha['População (Censo 2022)'] / linha['Área (km²)'])

df['Densidade Populacional (2022)'] = df.apply(calc_densidade, axis=1)
df

# %%

def prioritario (linha: pd.Series):
    if (linha['Densidade Populacional (2022)'] >= 100):
        return True
    else:
        return False

df['Prioritario'] = df.apply(prioritario, axis=1)
df

# %%