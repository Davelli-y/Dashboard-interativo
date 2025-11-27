# 🎬 Dashboard Interativo: Análise de Tendências do Cinema

## 🚀 Visão Geral do Projeto

Este projeto consiste no desenvolvimento de um Dashboard Interativo utilizando a biblioteca **Streamlit**. O objetivo é aplicar conceitos fundamentais de Ciência de Dados para coletar, processar e visualizar informações do universo cinematográfico, fornecendo *insights* sobre tendências, popularidade e o desempenho de filmes ao longo dos anos.

### 👥 Público-Alvo
O dashboard é destinado a entusiastas de cinema, estudantes, críticos e curiosos que desejam explorar informações sobre filmes, compreender tendências de popularidade, identificar obras bem avaliadas e analisar a influência de fatores como gênero, ano de lançamento e avaliação pública no sucesso das produções.

### 🎯 Justificativa da Escolha do Tema
O cinema é uma das indústrias culturais mais influentes do mundo. Com o crescimento de plataformas de *streaming*, compreender tendências, preferências e padrões de consumo é fundamental. A análise de dados cinematográficos permite revelar informações valiosas, como gêneros preferidos, *performances* de bilheteria e a evolução das avaliações. O tema escolhido une **relevância social, interesse coletivo e excelente disponibilidade de dados para exploração**.

---

## 💾 Dados e API

### Fonte da API de Dados
Os dados brutos para esta análise foram obtidos através da **TMDB API (The Movie Database)**.

* **API Utilizada:** [TMDB - The Movie Database](https://www.themoviedb.org/documentation/api)
* **Descrição dos Dados:** A TMDB é uma fonte de dados colaborativa e aberta, fornecendo informações detalhadas sobre milhares de filmes, incluindo títulos, datas de lançamento, gêneros, popularidade, votação média, orçamento, elenco e equipes de produção. O dashboard foca principalmente em filmes populares e bem avaliados para as análises.

### Processamento e Armazenamento
Os dados foram coletados via API e passaram pelas seguintes etapas de processamento antes de serem carregados no Streamlit:
1.  **Coleta:** Extração de dados via requisições HTTP para a API TMDB.
2.  **Limpeza:** Tratamento de valores nulos (NaN), padronização de formatos e conversão de tipos de dados.
3.  **Transformação:** Desaninhamento de colunas complexas (como a lista de gêneros), agregação de dados e criação de métricas auxiliares.
4.  **Armazenamento:** Os dados processados foram salvos no formato **`.csv`** (ou `.json`) para garantir a persistência e a velocidade de carregamento pelo dashboard.

---

## ❓ Perguntas-Chave do Dashboard

O dashboard foi construído com o objetivo de gerar *insights* e responder às seguintes questões centrais:

1.  Quais gêneros cinematográficos são mais populares atualmente e como essa popularidade evoluiu ao longo dos anos?
2.  Quais filmes apresentam as melhores avaliações do público e quais fatores podem estar associados a essas notas (como gênero, ano ou orçamento)?
3.  Existe alguma relação entre o ano de lançamento de um filme e sua popularidade, nota média ou volume de produções?
4.  Quais atores e diretores aparecem com maior frequência em filmes bem avaliados ou populares?
5.  Qual é a distribuição de filmes por gênero e quais deles predominam entre os mais bem avaliados?

---

## 💻 Como Rodar o Projeto Localmente

Siga os passos abaixo para executar o Dashboard Interativo em sua máquina local.

### 1. Pré-requisitos
Certifique-se de ter o Python (versão 3.8+) instalado.

### 2. Clonar o Repositório
```bash
git clone https://github.com/Davelli-y/Dashboard-interativo
3. Instalar Dependências
As bibliotecas necessárias estão listadas no arquivo requirements.txt. Instale-as usando pip:

Bash

pip install -r requirements.txt
4. Executar o Dashboard
Execute o script principal do Streamlit (assumindo que o arquivo se chama app.py):

Bash

streamlit run app.py
