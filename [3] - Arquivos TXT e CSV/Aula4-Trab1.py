# Faça uma função que leia o arquivo notas.txt (nome na primeira linha e notas na segunda). Imprima na tela a média de cada nome.

# 2. Depois adicione itens no arquivo texto

'''
    ---------   VERSAO 1     ----------
    
with open("notas.txt", "r") as arquivo:
    texto = arquivo.readline().rstrip() # o rstrip() retira o pular linha
    print(texto)
    valores = arquivo.readline().split() #pega os valores separados
    soma = float(valores[0]) + float(valores[1]) + float(valores[2])
    media = soma/3
    print(media)
    print(alunos)
    
'''

def media_alunos(arquivo):
    with open("notas.txt","r") as arquivo:
        linhas = arquivo.readlines() # le todo o arquivo e coloca em uma lista
        # iterando pelas linhas e calculando a media para cada aluno
        for i in range(0, len(linhas),2): # o loop começa em 0 e vai de 2 em 2 até o tamanho de linhas
            nome = linhas[i].strip() # tira os espaços em branco (o \n)
            notas = linhas[i+1].strip().split() # pega os valores separados
            # calculando a media
            notas = [float(nota) for nota in notas]
            media = sum(notas)/len(notas)
            print(f"A média de {nome} é: {media:.2f}")
            
media_alunos("notas.txt")

resposta = input("Deseja acrescentar mais alunos no arquivo? ")

if resposta == "sim":
    with open ("notas.txt", "a") as arquivo:
        nome = input("Nome do aluno: ")
        arquivo.write("\n" + nome)
        notas = input("Digite as 3 notas: ")
        arquivo.write("\n" + notas)
elif resposta == "nao":
    pass # nao faz nada
