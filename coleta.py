import requests
import pandas as pd

API_KEY = "fb95e0b8ec476b215572c0e909ce83fa"
URL = "https://api.themoviedb.org/3/movie/popular"

def coletar_filmes(paginas=5):
    """
    Coleta filmes populares da API TMDB
    e retorna uma lista de dicionários.
    """
    filmes = []

    for pagina in range(1, paginas + 1):
        params = {
            "api_key": API_KEY,
            "language": "pt-BR",
            "page": pagina
        }

        resposta = requests.get(URL, params=params)

        if resposta.status_code == 200:
            dados = resposta.json()["results"]
            for filme in dados:
                filmes.append({
                    "id": filme["id"],
                    "titulo": filme["title"],
                    "popularidade": filme["popularity"],
                    "nota": filme["vote_average"],
                    "votos": filme["vote_count"],
                    "data_lancamento": filme["release_date"],
                    "descricao": filme["overview"]
                })
        else:
            print("Erro ao acessar TMDB:", resposta.status_code)

    return filmes

def salvar_csv(filmes, nome_arquivo="data/filmes.csv"):
    df = pd.DataFrame(filmes)
    df.to_csv(nome_arquivo, index=False, encoding="utf-8")
    print(f"Arquivo salvo com sucesso: {nome_arquivo}")

if __name__ == "__main__":
    filmes = coletar_filmes(paginas=5)  # coleta 100 filmes (5 páginas x 20)
    salvar_csv(filmes)
