# 🎬 Dashboard Interativo de Filmes
**Análise de popularidade, avaliações e tendências do cinema utilizando dados da API TMDB**

---

## 📌 Sobre o Projeto
Este projeto apresenta um **dashboard interativo desenvolvido em Python com Streamlit** que permite analisar dados sobre filmes populares, suas avaliações, popularidade, ano de lançamento e outros indicadores relevantes.

Utilizando dados fornecidos pela **API pública TMDB (The Movie Database)**, o dashboard demonstra como técnicas básicas de Ciência de Dados podem ser aplicadas para coletar, armazenar, tratar e visualizar informações, possibilitando **insights sobre o comportamento da indústria cinematográfica** e as preferências do público.

---

## 👥 Público-Alvo
Projetado para:

- 🎞️ Entusiastas de cinema  
- 🎓 Estudantes de Tecnologia e Ciência de Dados  
- 📝 Críticos e criadores de conteúdo  
- 🔍 Curiosos que desejam explorar dados sobre filmes

---

## 🎯 Objetivo Geral
Explorar o universo cinematográfico por meio de dados públicos, respondendo perguntas que auxiliem na identificação de **tendências, padrões e insights relevantes** sobre a produção e consumo de filmes.

---

## ❓ Perguntas-Chave Respondidas pelo Dashboard

- 🎭 Quais gêneros são mais populares atualmente e como essa popularidade evoluiu ao longo dos anos?  
- ⭐ Quais filmes apresentam as melhores avaliações do público e o que influencia essas notas?  
- 📅 Existe relação entre o ano de lançamento e a popularidade, nota média ou quantidade de produções lançadas?  
- 🎬 Quais atores ou diretores aparecem com maior frequência entre filmes bem avaliados?  
- 🍿 Qual a distribuição de filmes por gênero e quais predominam entre os mais bem avaliados?

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia  | Uso |
|-------------|-----|
| Python      | Linguagem base do projeto |
| TMDB API    | Coleta de dados públicos |
| Pandas      | Limpeza e manipulação dos dados |
| Requests    | Consumo da API |
| Streamlit   | Criação do dashboard interativo |
| Plotly      | Visualização de dados e gráficos |
| CSV         | Armazenamento local dos dados tratados |

---

## 🔗 Fonte dos Dados
**Plataforma:** The Movie Database (TMDB)  
**Endpoint utilizado:** `/movie/popular`  
**Acesso:** Gratuito mediante chave de API  

**Dados coletados incluem:**  
Título • Popularidade • Nota média • Número de votos • Data de lançamento • Descrição

---

## 📂 Estrutura do Projeto

dashboard-filmes/
│
├── app.py               # Dashboard desenvolvido em Streamlit
├── coleta.py            # Coleta e armazenamento dos dados da API TMDB
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação do projeto
│
└── data/
    └── filmes.csv       # Dados coletados da API TMDB


---

## ▶️ Como Executar o Projeto

### 📥 1) Clonar o repositório

git clone https://github.com/davelli-y/dashboard-interativo.git
cd dashboard-interativo


📦 2) Instalar as dependências

pip install -r requirements.txt
🎬 3) Coletar os dados

python coleta.py
🚀 4) Executar o dashboard

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

🔸 Popularidade não significa qualidade: filmes muito populares nem sempre possuem ótimas avaliações.

🔸 Os filtros permitem identificar rapidamente filmes de destaque conforme critérios personalizados.

📸 Capturas de Tela do Dashboard

1️⃣ Visão Geral

Tela inicial com métricas principais de popularidade e desempenho dos filmes.

![3](https://github.com/user-attachments/assets/630ff506-1395-4de2-bd18-6e95569a9f47)

![4](https://github.com/user-attachments/assets/36949138-357a-45b3-93fb-66217bec0c98)

![5](https://github.com/user-attachments/assets/7e4cf545-b5df-4cc1-b95c-8b4645b31e20)

![6](https://github.com/user-attachments/assets/1b2534e8-eb47-423f-bb5a-5ab9b264536a)

2️⃣ Gráfico de Popularidade 

Demonstração de filtros interativos 

![1](https://github.com/user-attachments/assets/ffe726bf-09d6-4952-a4f3-076f5a1c00c8)

![2](https://github.com/user-attachments/assets/9e6a8a57-2303-4ab7-bdbe-ff6eaa228421)


📅 Entrega Final
Este repositório atende a todos os requisitos do projeto:

✔️ Uso de API pública
✔️ Armazenamento e tratamento local dos dados
✔️ Dashboard Interativo com Streamlit
✔️ Visualizações e KPIs
✔️ Documentação completa

👤 Integrantes do Grupo
Guilherme Henrique Yamaguchi Davelli

Alexandre Anzolin de Oliveira

Daniel Lopes da Silva
