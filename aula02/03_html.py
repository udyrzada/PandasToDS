# %%

import pandas as pd
import requests
from io import StringIO

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
}

# Aqui definimos um User-Agent apenas para o navegador confiar na requisição, caso contrário da erro 403: Forbidden.

resposta = requests.get(url, headers=headers) # Passamos o U-A como parâmetro no cabeçalho da requisição

dfs = pd.read_html(StringIO(resposta.text)) 
# type(dfs) # Nos retorna uma lista de DataFrames
len(dfs)
df = dfs[1]
df

df.to_csv('../Data/UFs.csv', index=False)
# type(df) # Nos retorna um único DataFrame

# %%

import pandas as pd

UFs = pd.read_csv('../Data/UFs.csv', sep=',')

UFs