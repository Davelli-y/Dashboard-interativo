import streamlit as st
import pandas as pd
import plotly.express as px

# ========== Carregar dados ==========
@st.cache_data
def carregar_dados():
    return pd.read_csv("data/filmes.csv")

df = carregar_dados()

# ========== Configurações iniciais ==========
st.set_page_config(
    page_title="Dashboard de Filmes",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Dashboard Interativo de Filmes")
st.markdown("Análise de popularidade, notas e tendências do cinema usando dados da TMDB API.")

# ========== KPIs ==========
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Quantidade de Filmes", df.shape[0])

with col2:
    st.metric("Média de Notas", round(df["nota"].mean(), 2))

with col3:
    st.metric("Popularidade Média", round(df["popularidade"].mean(), 2))

st.divider()

# ========== Filtro Interativo: Ano ==========
df["ano"] = pd.to_datetime(df["data_lancamento"], errors='coerce').dt.year
anos = df["ano"].dropna().unique()
anos_selecionados = st.slider("Selecione o intervalo de anos", int(df["ano"].min()), int(df["ano"].max()), (2010, 2025))

df_filtrado = df[(df["ano"] >= anos_selecionados[0]) & (df["ano"] <= anos_selecionados[1])]

st.subheader("Filmes dentro do intervalo selecionado")
st.write(df_filtrado[["titulo", "ano", "nota", "popularidade"]])

# ========== Gráfico de Popularidade ==========
fig = px.bar(df_filtrado.sort_values(by="popularidade", ascending=False).head(10),
             x="titulo",
             y="popularidade",
             title="Top 10 filmes mais populares",
             labels={"titulo": "Título", "popularidade": "Popularidade"})

st.plotly_chart(fig, use_container_width=True)

# ========== Gráfico de Notas ==========
fig2 = px.scatter(df_filtrado,
                  x="ano",
                  y="nota",
                  size="popularidade",
                  title="Distribuição das notas por ano",
                  labels={"ano": "Ano", "nota": "Nota"})
st.plotly_chart(fig2, use_container_width=True)
st.divider()

# ========== Filtro Interativo: Nota mínima ==========
nota_minima = st.slider("Selecione a nota mínima", 0.0, 10.0, 7.0)
df_nota = df_filtrado[df_filtrado["nota"] >= nota_minima]

st.subheader(f"Filmes com nota acima de {nota_minima}")
st.write(df_nota[["titulo", "ano", "nota", "popularidade"]])

# ========== Gráfico: Média de notas por ano ==========
media_anos = df_filtrado.groupby("ano")["nota"].mean().reset_index()

fig3 = px.line(media_anos,
               x="ano",
               y="nota",
               markers=True,
               title="Média das notas dos filmes por ano",
               labels={"ano": "Ano", "nota": "Nota média"})

st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ========== Insights ==========
st.subheader("📌 Insights Gerais")

st.markdown("""
- A média de notas por ano permite identificar períodos de maior qualidade percebida pelo público.
- O filtro por nota e ano ajuda a encontrar filmes mais relevantes segundo critérios pessoais.
- Filmes mais populares nem sempre possuem as melhores avaliações, mostrando que popularidade e qualidade são fatores distintos.
""")
