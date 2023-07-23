# Leia 2 matrizes de números reais e calcule a matriz resultante da soma das 2 primeiras. Imprima o resultado com 2 casas decimais.

## Função para ler matriz

def lerMatriz(linha, coluna):
    matriz = []
    for i in range(linha):
        linha = []
        for j in range(coluna):
            valor = float(input("Digite o valor da posição [%d][%d]: " % (i,j)))
            linha.append(valor)
        matriz.append(linha)
    return matriz

# Lendo as matrizes 

n = int(input("Quantas LINHAS tem as matrizes? "))
m = int(input("Quantas COLUNAS tem as matrizes? "))

print("\nPrimeira matriz: ")
matriz1 = lerMatriz(n,m)

print("\nSegunda matriz: ")
matriz2 = lerMatriz(n,m)

# Somando as matrizes

matriz_soma = []

for i in range(n):
    linha = []
    for j in range(m):
        soma = matriz1[i][j] + matriz2[i][j]
        linha.append(soma)
    matriz_soma.append(linha)

# Imprimindo a soma

print("\nA soma das matrizes é: ")
for linha in matriz_soma:
    print(["%.2f" % valor for valor in linha])

