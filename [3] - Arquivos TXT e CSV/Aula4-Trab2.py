# Faça um programa que leia o arquivo "SCOPUS.CSV" no qual representa publicações da área de CC em revistas acadêmicas.
# Imprima na tela o nome dos autores das publicações com mais de 20 citações.

import csv
with open("scopus.csv","r", encoding ="utf-8-sig") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)
    for linha in leitor:
            nome = linha[0].split(",")
            citacoes = linha[11].strip()
            if citacoes.isdigit() and int(citacoes) > 20:
                print(nome)

