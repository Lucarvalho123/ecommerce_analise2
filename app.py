# app.py
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html

# Passo 1: Ler o CSV
df = pd.read_csv("ecommerce_estatistica.csv")

# Passo 2: Criar os gráficos usando Plotly

# Histograma
fig_hist = px.histogram(df, x="Nota", nbins=10, title="Distribuição das Notas dos Produtos")
fig_hist.update_layout(xaxis_title="Nota", yaxis_title="Frequência")

# Dispersão
fig_scatter = px.scatter(df, x="N_Avaliações", y="Nota", color="Gênero", title="Número de Avaliações vs Nota")
fig_scatter.update_layout(xaxis_title="Número de Avaliações", yaxis_title="Nota")

# Mapa de calor da correlação
corr = df.corr(numeric_only=True)
fig_heatmap = go.Figure(data=go.Heatmap(
    z=corr.values,
    x=corr.columns,
    y=corr.columns,
    colorscale='Viridis'
))
fig_heatmap.update_layout(title="Mapa de Calor - Correlação entre Variáveis")

# Gráfico de barras - Top 10 marcas por número de avaliações
top_marcas = df.groupby("Marca")["N_Avaliações"].sum().sort_values(ascending=False).head(10)
fig_bar = px.bar(x=top_marcas.values, y=top_marcas.index, orientation='h',
                 title="Top 10 Marcas com Maior Número de Avaliações")
fig_bar.update_layout(xaxis_title="Número de Avaliações", yaxis_title="Marca")

# Gráfico de pizza - Distribuição por Gênero
genero_counts = df["Gênero"].value_counts()
fig_pie = px.pie(values=genero_counts.values, names=genero_counts.index,
                 title="Distribuição dos Produtos por Gênero")

# Gráfico de densidade
fig_density = px.density_contour(df, x="Nota", title="Densidade das Notas dos Produtos")
fig_density.update_layout(xaxis_title="Nota", yaxis_title="Densidade")

# Gráfico de regressão (scatter + linha)
fig_reg = px.scatter(df, x="N_Avaliações", y="Nota", trendline="ols",
                     title="Regressão Linear: Nota vs Número de Avaliações")
fig_reg.update_layout(xaxis_title="Número de Avaliações", yaxis_title="Nota")

# Passo 3: Criar a aplicação Dash
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Análise de Ecommerce"),

    dcc.Graph(id="histograma", figure=fig_hist),
    dcc.Graph(id="dispersao", figure=fig_scatter),
    dcc.Graph(id="mapa_calor", figure=fig_heatmap),
    dcc.Graph(id="barra", figure=fig_bar),
    dcc.Graph(id="pizza", figure=fig_pie),
    dcc.Graph(id="densidade", figure=fig_density),
    dcc.Graph(id="regressao", figure=fig_reg),
])

if __name__ == "__main__":
    app.run(debug=True)

