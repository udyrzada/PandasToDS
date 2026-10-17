# %%

import pandas as pd
from math import *

transacoes = pd.read_csv('../Data/transacoes.csv', sep=';')

transacoes.head(3)

# %%

# sqrt((amplitude - media) ** 2)

def diff_amp(valor: pd.Series):
    amplitude = valor.max() - valor.min()
    media = valor.mean()
    quadrado = ((amplitude - media) ** 2)
    final = sqrt(quadrado)
    return final

lista_idades = [10, 20, 30 ,40, 50]
serie = pd.Series(lista_idades)

diff_amp(serie)

# %%

summary = transacoes.groupby('IdCliente', as_index=False).aggregate(
    {'QtdePontos': ['sum', 'mean', diff_amp],
     'IdTransacao': ['count']})

summary

# %%

summary.columns = ['IdCliente', 'SomaPontos', 'MediaPontos', 'DiffAmpPontos', 'QuantidadeTransacoes']

summary

# %%
