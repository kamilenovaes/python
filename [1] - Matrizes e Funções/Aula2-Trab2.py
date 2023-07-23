# Faça uma função que leia uma lista de inteiros e crie uma segunda lista com os elementos pares da primeira. Imprima as duas.

# Função de elementos pares 
def elementosPares(lista):
    pares = [x for x in lista if x % 2 == 0]
    return pares

# Lendo uma lista
# Se digitar vazio, para de ler a lista

lista = []
print("\nDigite a lista. Se for vazio (apenas ENTER), a lista acaba.")
while True:
    valor = input("Digite um número inteiro: ")
    if valor == "":
        break
    lista.append(int(valor))

pares = elementosPares(lista)

#Imprimindo resultado

print("\nLista original:", lista)
print("Lista de pares:", pares)