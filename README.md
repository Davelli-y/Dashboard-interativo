# 🎬 Dashboard Interativo de Filmes
**Análise de popularidade, avaliações e tendências do cinema utilizando dados da API TMDB**

## 📌 Sobre o Projeto
Este projeto apresenta um **dashboard interativo desenvolvido em Python com Streamlit**, que permite analisar dados sobre filmes populares, suas avaliações, popularidade, ano de lançamento e outros indicadores relevantes.

Utilizando dados fornecidos pela **API pública TMDB (The Movie Database)**, o dashboard demonstra como técnicas básicas de Ciência de Dados podem ser aplicadas para coletar, armazenar, tratar e visualizar informações, possibilitando **insights sobre o comportamento da indústria cinematográfica** e as preferências do público.

## 👥 Público-Alvo
Projetado para:

- 🎞️ Entusiastas de cinema  
- 🎓 Estudantes de Tecnologia e Ciência de Dados  
- 📝 Críticos e criadores de conteúdo  
- 🔍 Curiosos que desejam explorar dados sobre filmes

## 🎯 Objetivo Geral
Explorar o universo cinematográfico por meio de dados públicos, respondendo perguntas que auxiliem na identificação de **tendências, padrões e insights relevantes** sobre a produção e consumo de filmes.

## ❓ Perguntas-Chave Respondidas pelo Dashboard

- 🎭 Quais gêneros são mais populares atualmente e como essa popularidade evoluiu ao longo dos anos?  
- ⭐ Quais filmes apresentam as melhores avaliações do público e o que influencia essas notas?  
- 📅 Existe relação entre o ano de lançamento e a popularidade, nota média ou quantidade de produções lançadas?  
- 🎬 Quais atores ou diretores aparecem com maior frequência entre filmes bem avaliados?  
- 🍿 Qual a distribuição de filmes por gênero e quais predominam entre os mais bem avaliados?

## 🛠️ Tecnologias Utilizadas

| Tecnologia  | Uso |
|-------------|-----|
| **Python**   | Linguagem base do projeto |
| **TMDB API** | Coleta de dados públicos |
| **Pandas**   | Limpeza e manipulação dos dados |
| **Requests** | Consumo da API |
| **Streamlit**| Criação do dashboard interativo |
| **Plotly**   | Visualização de dados e gráficos |
| **CSV**      | Armazenamento local dos dados tratados |

## 🔗 Fonte dos Dados

- **Plataforma:** *The Movie Database (TMDB)*  
- **Endpoint utilizado:** `/movie/popular`  
- **Acesso:** Gratuito mediante chave de API  

**Dados coletados:**  
Título • Popularidade • Nota média • Número de votos • Data de lançamento • Descrição

## 📂 Estrutura do Projeto

/dashboard-filmes
│ app.py                 # Dashboard Streamlit
│ coleta.py              # Coleta e armazenamento dos dados
│ requirements.txt       # Dependências do projeto
│ README.md              # Documentação
│ data/
│   filmes.csv           # Dados coletados da API TMDB


▶️ Como Executar o Projeto
1️⃣ Instale as dependências
pip install -r requirements.txt

2️⃣ Gere o arquivo CSV dos filmes
python coleta.py

3️⃣ Inicie o dashboard
streamlit run app.py

O navegador abrirá automaticamente exibindo o dashboard.

📊 Recursos do Dashboard
✔️ KPIs de destaque
✔️ Filtro interativo por Ano
✔️ Filtro por Nota mínima
✔️ Listagem dinâmica de filmes filtrados
✔️ Top 10 filmes mais populares
✔️ Distribuição das notas por ano
✔️ Média das notas por ano

📌 Insights Obtidos
🔸 A média das notas ao longo dos anos indica períodos com maior aprovação do público.

🔸 Popularidade não significa qualidade: filmes muito populares nem sempre têm as melhores notas.

🔸 Os filtros permitem identificar rapidamente filmes de destaque conforme critérios personalizados.

### 📸 Capturas de Tela do Dashboard

**[Inserir Captura de Tela 1: Visão Geral e KPIs]**
*Descrição: Tela inicial do dashboard mostrando os principais indicadores de popularidade e a distribuição geral de filmes.*

**[Inserir Captura de Tela 2: Interatividade e Gráfico de Gêneros]**
*Descrição: Demonstração da interatividade com o filtro de Nota Mínima, e o gráfico da evolução de Popularidade por Gênero.*

📅 Entrega Final
Este repositório atende a todos os requisitos do projeto:
✔️ Uso de API pública
 ✔️ Armazenamento e tratamento local dos dados
 ✔️ Dashboard Interativo com Streamlit
 ✔️ Visualizações e KPIs
 ✔️ Documentação completa

👤 Integrantes do Grupo
Guilherme Henrique Yamaguchi Davelli
Alexandre Oliveira
Daniel Lopes



