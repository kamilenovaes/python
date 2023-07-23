# Faça um programa que leia a informação (nome, marca, quilometragem) de 3 carros e armazene em uma lista. Imprima a lista.

# Inicializando a lista e os dicionários
L = []
a = {}
b = {}
c = {}

print("\nPRIMEIRO CARRO:")
a["nome"] = input("Nome: ")
a["marca"] = input("Marca: ")
a["km"] = input("Quilometragem: ")

L.append(a)

print("\nSEGUNDO CARRO:")
b["nome"] = input("Nome: ")
b["marca"] = input("Marca: ")
b["km"] = input("Quilometragem: ")

L.append(b)

print("\nTERCEIRO CARRO:")
c["nome"] = input("Nome: ")
c["marca"] = input("Marca: ")
c["km"] = input("Quilometragem: ")

L.append(c)

print("\n")
print(L)