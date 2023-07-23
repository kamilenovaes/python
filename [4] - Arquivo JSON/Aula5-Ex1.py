# Imprimir o nome do curso e o nome dos alunos. (arquivo teste2.json)

import json
with open("teste2.json","r", encoding = "utf-8") as arq_json:
    dados = json.load(arq_json)
    print(dados["Curso"])
    for item in dados["Alunos"]:
        print(item["nome"])