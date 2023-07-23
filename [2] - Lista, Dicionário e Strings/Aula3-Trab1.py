# Faça um programa que manipule uma lista de funcionários (cada funcionário deve ser armazenado em um dicionário).
# Um funcionário tem como campos obrigatórios seu "nome", "CPF" e "cargo". Como campos opcionais "telefone" e "e-mail".
# Os campos não fornecidos não devem aparecer no dicionário. Imprima todos os funcionários cujo o nome começa com "A" ou "B"
# e que forneceu telefone.

lista_funcionarios = [
    {"nome" : "Ana", "CPF" : "123.456.789-00", "cargo" : "Secretária", "telefone" : "(21) 987001234", "email" : "ana@teste.com"},
    {"nome" : "Julio", "CPF": "987.654.321-99", "cargo": "Assistente", "email": "julio@teste.com"},
    {"nome" : "Beatriz", "CPF": "456.123.789-22", "cargo": "Estagiária", "telefone": "(22) 995004321"},
    {"nome" : "Andre", "CPF": "321.654.987-77", "cargo": "Recepcionista"},
    {"nome" : "Bernardo", "CPF": "564.321.879-11", "cargo": "Gerente", "telefone": "(22) 978002134", "email": "bernardo@teste.com"}
   
]

# get("nome") acessa o valor do campo "nome" e retorna o valor associado à chave

for funcionario in lista_funcionarios:
    if funcionario.get("nome")[0].lower() in ["a", "b"] and funcionario.get("telefone") is not None:
        print(funcionario)
