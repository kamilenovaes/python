# Aluna: Kamile de Souza Novaes

# Faça um programa que leia uma string a qual representa um diretório de um S.O. 
# Gere um arquivo JSON com todos os arquivos desse diretório, dos seus diretórios filhos e etc.

import json
import os  #permite manipular diretórios e arquivos

# função recursiva para percorrer os diretórios
def percorre_diretorios(diretorio):
    # inicializa o tipo de formatação do dicionário
    arquivos_dir = {"Nome": os.path.basename(diretorio), "Arquivos": [], "Diretorios": []}
    
    # gera uma lista com os nomes dos arquivos e diretórios
    for nome_arq in os.listdir(diretorio):
        
        # concatena o diretorio com o nome do arquivo
        caminho = os.path.join(diretorio, nome_arq)
        
        #verifica se o caminho corresponde a um arquivo, e armazena na variavel
        if os.path.isfile(caminho):
            arquivos_dir["Arquivos"].append(nome_arq)
            
        # verifica se o caminho corresponde a um diretorio (no caso, subdiretorio)    
        elif os.path.isdir(caminho):
            # chama recursivamente, e adiciona na variavel
            subarquivos_dir = percorre_diretorios(caminho)
            arquivos_dir["Diretorios"].append(subarquivos_dir)
    
    return arquivos_dir

diretorio = input("Diretorio: ")
arquivo = percorre_diretorios(diretorio)

# gerando o arquivo json
nomeJSON = input("Nome do arquivo JSON: ")

with open(nomeJSON, 'w') as file:
    json.dump(arquivo, file, indent=3)
    
print("OK!")
        