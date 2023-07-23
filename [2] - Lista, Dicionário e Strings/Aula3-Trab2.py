# Faça um programa que leia uma lista de carros (cada carro é um dicionário que contém "nome" e "marca").
# Imprima a lista ordenada decrescentemente pela marca do carro.

lista_carros = [
    {"nome": "Uno", "marca": "Fiat"},
    {"nome": "Ka", "marca": "Ford"},
    {"nome": "A3", "marca": "Audi"},
    {"nome": "Astra", "marca": "Chevrolet"},
    {"nome": "Captur", "marca": "Renault"},
    {"nome": "Jetta", "marca": "Volkswagen"},
    {"nome": "Hilux", "marca": "Toyota"},
    {"nome": "C3", "marca": "Citroen"},
    {"nome": "Range Rover", "marca": "Land Rover"},
    {"nome": "911", "marca": "Porsche"}
]

# função sorted() = sorted(sequencia, key=None, reverse=False)
# key é opcional e especifica uma função de chave para personalizar a ordem de classificação
# o parâmetro lambda é utilizado para criar uma função anônima que extrai a chave desejada do dicionário de cada carro
# o parâmetro x representa cada elemento da lista de carros e x["marca"] extrai a marca do carro para cada elemento

ordenados_decrescente = sorted(lista_carros, key=lambda x: x["marca"], reverse=True)

for carro in ordenados_decrescente:
    print(carro["nome"], carro["marca"])
