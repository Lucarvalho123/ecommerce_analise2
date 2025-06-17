# Análise de Dados do E-commerce

# Importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração de estilo
df = pd.read_csv("ecommerce_estatistica.csv")
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Visualização inicial dos dados
print(df.head())
print(df.info())
print(df.describe())

# Verificação de dados ausentes
print(df.isnull().sum())

# ----------------------------
# GRÁFICO 1 - HISTOGRAMA
sns.histplot(df["Nota"], bins=10, kde=True, color="skyblue")
plt.title("Distribuição das Notas dos Produtos")
plt.xlabel("Nota")
plt.ylabel("Frequência")
plt.grid(True)
plt.show()

# ----------------------------
# GRÁFICO 2 - DISPERSÃO
sns.scatterplot(x="N_Avaliações", y="Nota", data=df, hue="Gênero", alpha=0.7)
plt.title("Relação entre Número de Avaliações e Nota")
plt.xlabel("Número de Avaliações")
plt.ylabel("Nota")
plt.legend(title="Gênero")
plt.grid(True)
plt.show()

# ----------------------------
# GRÁFICO 3 - MAPA DE CALOR
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Mapa de Calor - Correlação entre Variáveis Numéricas")
plt.show()

# ----------------------------
# GRÁFICO 4 - BARRAS (Top 10 marcas com mais avaliações)
top_marcas = df.groupby("Marca")["N_Avaliações"].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_marcas.values, y=top_marcas.index, palette="viridis")
plt.title("Top 10 Marcas com Maior Número de Avaliações")
plt.xlabel("Total de Avaliações")
plt.ylabel("Marca")
plt.grid(True, axis='x')
plt.show()

# ----------------------------
# GRÁFICO 5 - PIZZA (Distribuição por Gênero)
df["Gênero"].value_counts().plot.pie(autopct="%1.1f%%", startangle=90, shadow=True)
plt.title("Distribuição dos Produtos por Gênero")
plt.ylabel("")
plt.show()

# ----------------------------
# GRÁFICO 6 - DENSIDADE
sns.kdeplot(df["Nota"], shade=True, color="purple")
plt.title("Densidade das Notas dos Produtos")
plt.xlabel("Nota")
plt.ylabel("Densidade")
plt.grid(True)
plt.show()

# ----------------------------
# GRÁFICO 7 - REGRESSÃO
sns.regplot(x="N_Avaliações", y="Nota", data=df, scatter_kws={'alpha':0.4}, line_kws={'color':'red'})
plt.title("Regressão Linear: Nota vs Número de Avaliações")
plt.xlabel("Número de Avaliações")
plt.ylabel("Nota")
plt.grid(True)
plt.show()
