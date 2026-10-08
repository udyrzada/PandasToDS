# %%

import pandas as pd

# Pega os dados que estão copiados no CTRL+C. É para ser mais experimental e investigativo do que produtivo. Especialmente util para pesquisas rápidas

df = pd.read_clipboard(sep=';')
df