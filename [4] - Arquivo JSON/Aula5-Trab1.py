# Para cada curso existente no "teste3.json", imprima o nome do curso e o nome dos seus alunos.

import json
print()

with open('teste3.json', 'r', encoding="utf-8") as file:
    dados = json.load(file)

# percorre a lista de cursos
for curso in dados:
    nome_curso = curso['Curso']
    print("Curso -", nome_curso)
    
    # percorre os alunos do curso
    alunos = curso['Alunos']
    for aluno in alunos:
        nome_aluno = aluno['nome']
        print("Aluno:", nome_aluno)

    print()