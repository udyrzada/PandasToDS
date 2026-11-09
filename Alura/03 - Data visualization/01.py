# %%

import pandas as pd

df = pd.read_csv('../Data/canadian_immegration_data.csv')

df.head()

# %%

df.info()

# %%

df.set_index(df['Country'], inplace=True)
df.head()

# %%

df.drop(columns='Country', inplace=True)
df.head()

# %%

anos = df.columns.to_list()
anos = anos[3:-1]
anos

# %%

brasil = df.loc['Brazil', anos]
brasil

# %%

brasil_dict = {'ano': anos, 'imigrantes': brasil.values.tolist()}
brasil_dict

# %%

dados_brasil = pd.DataFrame(brasil_dict)
dados_brasil.head()

# %%

import matplotlib.pyplot as plt

plt.figure(figsize=(8,4))
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
plt.title('Imigração do Brasil para o Canadá')
plt.xlabel('Ano')
plt.ylabel('Imigrantes')
plt.xticks(anos[::5])
plt.show()

# %%

fig, ax = plt.subplots(figsize=(8,4))

# Fig --> Permite a criação de uma tela em branco
# Ax --> Determina os eixos X e Y

ax.plot(dados_brasil['ano'], dados_brasil['imigrantes'])
ax.set_title('Imigração do Brasil para o Canadá\n(1980 - 2013)')
ax.set_xlabel('Ano')
ax.set_ylabel('Imigrantes')
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
plt.show()

# %%

# Criando uma imagem com mais de um gráfico

# Gráfico 1
fig, axs = plt.subplots(1, 2, figsize=(15,5))
axs[0].plot(dados_brasil['ano'], dados_brasil['imigrantes'])
axs[0].set_title('Imigração do Brasil para o Canadá\n(1980 - 2013)')
axs[0].set_xlabel('Ano')
axs[0].set_ylabel('Imigrantes')
axs[0].xaxis.set_major_locator(plt.MultipleLocator(5))
axs[0].grid()

# Gráfico 2
axs[1].boxplot(dados_brasil['imigrantes'])
axs[1].set_title('Boxplot de imigração do Brasil para o Canadá\n(1980 - 2013)')
axs[1].set_xlabel('Brasil')
axs[1].set_ylabel('Número imigrantes')
axs[1].grid()
plt.show()

# %%

dados_brasil.describe()

# %%

# Criando uma imagem com 4 gráficos

fig, axs = plt.subplots(2,2,figsize=(10,6))
fig.subplots_adjust(hspace=0.5, wspace=0.3)
fig.suptitle('Imigração dos 4 maiores países da América do Sul para o Canadá\n (1980 - 2013)')

axs[0,0].plot(df.loc['Brazil', anos])
axs[0,0].set_title('Brasil')

axs[0,1].plot(df.loc['Colombia', anos])
axs[0,1].set_title('Colombia')

axs[1,0].plot(df.loc['Argentina', anos])
axs[1,0].set_title('Argentina')

axs[1,1].plot(df.loc['Peru', anos])
axs[1,1].set_title('Peru')

for ax in axs.flat:
    ax.xaxis.set_major_locator(plt.MultipleLocator(5))

for ax in axs.flat:
    ax.set_xlabel('Ano')
    ax.set_ylabel('Imigrantes')

ymin = 0
ymax = 7000

for ax in axs.ravel():
    ax.set_ylim(ymin, ymax)

plt.show()

# %%
