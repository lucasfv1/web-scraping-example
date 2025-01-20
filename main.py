# Importar e instalar as bibliotecas necessárias
from bs4 import BeautifulSoup
import requests

# Fazer requisição para a URL desejada e obter o conteúdo da página
response = requests.get("https://pt.wikipedia.org/wiki/Sandra_Bullock")

# Obter o texto da resposta
html_response = response.text

# Criar um objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(html_response, "html.parser")

# Obter a tabela com as informações de filmografia
tabela_filmografia = soup.find(name="table", class_="wikitable")

# Obter todas as linhas da tabela
todas_as_linhas = tabela_filmografia.find_all(name="tr")

# Criar uma lista para armazenar os dicionários de filmes
filmes = []

# Armazenar último ano encontrado (resolve problema do rowspan na primeira coluna das linhas)
ultimo_ano = None

# Iterar sobre as linhas da tabela pulando a primeira que é a de título
for linha in todas_as_linhas[1:]:
    # Obter as colunas da linha
    colunas = linha.find_all("td")

    # Verificar se a linha possui cinco colunas
    if len(colunas) == 5:
        # Atualizar o valor de ultimo_ano se existirem cinco colunas
        ultimo_ano = colunas[0].text.strip()

        # Criar o dicionário para cada filme quando a quantidade de colunas for igual a cinco
        filme = {
            "ano": ultimo_ano,
            "filme": colunas[1].text.strip(),
            "titulo_portugues": colunas[2].text.strip(),
            "papel": colunas[3].text.strip(),
            "direcao": colunas[4].text.strip(),
        }
    else:
        # Criar o dicionário para cada filme quando a quantidade de colunas for menor que cinco
        filme = {
            "ano": ultimo_ano,
            "filme": colunas[0].text.strip(),
            "titulo_portugues": colunas[1].text.strip(),
            "papel": colunas[2].text.strip(),
            "direcao": colunas[3].text.strip(),
        }

    # Adicionar o filme à lista
    filmes.append(filme)

# Imprimir a lista com os dicionários
for filme in filmes:
    print(filme)
