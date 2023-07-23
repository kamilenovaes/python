# Leia o arquivo "scopus.csv" e escreva o nome dos autores e o número de citações em um aquivo JSON das public. > 20 citações.

import csv
import json
import re

dados = []  

with open('scopus.csv', 'r', encoding ="utf-8-sig") as file:
    leitor = csv.reader(file)
    
    # percorre as linhas do csv
    for linha in leitor:
        nome = linha[0].split(",")
        citacoes = linha[11].strip()
        
        # remove os números entre barras em cada elemento da lista
        nome = [re.sub(r'\"[\d;]+\"', '', autor) for autor in nome]
        
        if citacoes.isdigit() and int(citacoes) > 20:
           # cria um dicionario e adiciona à lista de dados
            registro = {
                "Autores": nome,
                "Citações": int(citacoes)
            }
            dados.append(registro)

# criando a escrevendo no arquivo JSON
with open('scopusJSON.json', 'w', encoding = "utf-8") as file:
    json.dump(dados, file, indent=3, ensure_ascii=False)

print("OK!")