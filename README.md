🎬 Dashboard Interativo de Filmes
Análise de popularidade, avaliações e tendências do cinema usando dados da TMDB

📌 Sobre o Projeto
Este projeto apresenta um dashboard interativo desenvolvido em Python com Streamlit, que permite analisar dados sobre filmes populares, suas avaliações, popularidade, ano de lançamento e outros indicadores relevantes.
Utilizando dados fornecidos pela API pública TMDB (The Movie Database), o dashboard demonstra como técnicas básicas de Ciência de Dados podem ser aplicadas para coletar, armazenar, tratar e visualizar informações, possibilitando insights sobre o comportamento da indústria cinematográfica e preferências do público.

👥 Público-Alvo
O dashboard foi desenvolvido para entusiastas de cinema, estudantes, críticos e curiosos que desejam explorar informações sobre filmes, entender tendências de popularidade e identificar relações entre o ano de lançamento, notas e gêneros mais consumidos pelo público.

🎯 Objetivo Geral
Explorar o universo cinematográfico por meio de dados públicos, respondendo perguntas que auxiliem na identificação de tendências, padrões e insights relevantes sobre a produção e consumo de filmes.

❓ Perguntas-Chave Respondidas pelo Dashboard
O projeto se propõe a responder:
Quais gêneros cinematográficos são mais populares atualmente e como essa popularidade evoluiu ao longo dos anos?


Quais filmes apresentam as melhores avaliações do público e quais fatores estão associados a essas notas?


Existe relação entre o ano de lançamento de um filme e sua popularidade, nota média ou quantidade de produções?


Quais atores ou diretores aparecem com maior frequência em filmes bem avaliados?


Qual a distribuição de filmes por gênero e quais predominam entre os mais bem avaliados?



🛠️ Tecnologias Utilizadas
Tecnologia
Uso
Python
Linguagem base
TMDB API
Coleta de dados públicos
Pandas
Limpeza, manipulação e armazenamento dos dados
Requests
Consumo da API
Streamlit
Criação da interface interativa
Plotly
Visualização dos dados (gráficos interativos)
CSV
Armazenamento dos dados processados


🔗 Fonte dos Dados
API utilizada: The Movie Database (TMDB)
 Acesso gratuito mediante criação de chave na plataforma.
Endpoint utilizado: /movie/popular
Dados coletados:
Título


Popularidade


Nota do público


Número de votos


Data de lançamento


Descrição



📂 Estrutura do Projeto
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
 ✔️ Filtro interativo por Nota mínima
 ✔️ Listagem de filmes filtrados
 ✔️ Gráfico Top 10 filmes mais populares
 ✔️ Gráfico Distribuição de notas por ano
 ✔️ Gráfico Média das notas por ano

📌 Insights Obtidos
A média das notas ao longo dos anos possibilita identificar períodos com maior aprovação do público.


Popularidade e avaliação não são necessariamente relacionadas: filmes muito populares podem não ter as melhores notas.


Os filtros permitem identificar rapidamente filmes de destaque, conforme critérios personalizados do usuário.



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



