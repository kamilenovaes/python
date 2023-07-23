# Leia uma matriz 3x3, depois leia valor "x" e informe se "x" existe na matriz.

# lendo a matriz

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input("Digite o valor da posição [%d][%d]: " % (i,j)))
        linha.append(valor)
    matriz.append(linha)

# procurar o valor x

x = (int(input("Digite o valor a ser procurado: ")))

# verificando se existe x na matriz

encontrado = False
for i in range(3):
    for j in range(3):
        if matriz[i][j] == x:
            encontrado = True
            break
    if encontrado:
        break

# imprimindo resultado

if encontrado:
    print("O valor %d está na matriz." % x)
else:
    print("O valor %d NÃO está na matriz." % x)