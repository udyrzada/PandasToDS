# %%

# Objetivo ---> Normalizar o dataframe

import pandas as pd

df = pd.read_json('../Data/dados_hospedagem.json')

df.head()

# %%

df = pd.json_normalize(df['info_moveis']) # Normalizamos o aninhamento proveniente de arquivos .json
df.head()

# %%

# Objetivo ---> Desagrupar os dados (explode)

colunas = df.columns.to_list()
colunas[3:] # Colunas que precisam do método explode

# %%

df = df.explode(colunas[3:])
df.head()

# Agora foram criadas várias linhas a partir dos dados que estavam contidos nas listas. Agora existe um mesmo id para mais de uma linha

# %%

df.reset_index(drop=True, inplace=True)
df.head()

# %%

df.info()

# %%

inteiros = ['max_hospedes', 'quantidade_banheiros', 'quantidade_quartos', 'quantidade_camas']

df[inteiros] = df[inteiros].astype(int)
df.info()

# %%

df['avaliacao_geral'] = df['avaliacao_geral'].astype(float)
df.info()

# %%

def conv_cifrao_to_float(valor):
    return valor.str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)

numeros_cifrao = ['taxa_deposito', 'taxa_limpeza', 'preco']

df[numeros_cifrao] = df[numeros_cifrao].apply(conv_cifrao_to_float)
df.head(3)

# %%

df.info()

# %%

# Objetivo ---> Tokenização dos textos (limpar e separar)

df['descricao_local'] = df['descricao_local'].str.lower()
df['descricao_local']

# %%

df['descricao_local'][3169] # Possui virgula, ponto, barra ... etc

# %%

df['descricao_local'] = df['descricao_local'].replace('[^a-zA-Z0-9\-\']', ' ', regex=True).str.replace('(?<!\w)-(?!\w)', ' ', regex=True).str.split()

# %%

df['descricao_local'][3169] # Agora está limpo de caracteres indesejados

# %%

df.head(3)
# %%

df['comodidades'] = df['comodidades'].str.replace('\{|}|\"','', regex=True).str.split(',')

df['comodidades']

# %%

df.head()

# %%

df['descricao_vizinhanca'] = df['descricao_vizinhanca'].str.lower().str.replace('[^a-zA-Z0-9\-\']', ' ', regex=True).str.replace('(?<!\w)-(?!\w)', ' ', regex=True).str.split()

# %%

df['descricao_vizinhanca'][0]

# %%

