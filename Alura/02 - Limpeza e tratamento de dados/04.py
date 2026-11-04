# %%

# Get dummies

import pandas as pd

# Criando um DataFrame de exemplo
df = pd.DataFrame({'cor': ['vermelho', 'azul', 'verde', 'vermelho'],
                   'tamanho': ['pequeno', 'médio', 'grande', 'médio'],
                   'formato': ['quadrado', 'redondo', 'redondo', 'quadrado']})

# Transformando as colunas categóricas em variáveis numéricas binárias
df_dummies = pd.get_dummies(df, columns=['cor', 'tamanho'], prefix=['cor', 'tam'], prefix_sep='-', drop_first=True, dtype=int)

# Exibindo o DataFrame resultante
df_dummies

# %%

# A utilização do get_dummies() é particularmente útil quando é necessário a utilização apenas de dados numéricos ou booleanos, algo que é comumente visto no treinamento de modelos de aprendizado de máquina. Ou seja, utilizamos esse método quando queremos transformar variáveis qualitativas em quantitativas