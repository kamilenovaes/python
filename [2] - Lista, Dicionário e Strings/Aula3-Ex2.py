# Leia uma lista de 5 strings e depois imprima apenas as strings que contém "rio".
# Exemplos: casa, Rio das ostras, canário, Eucariontes, vaso

lista_strings = ["casa", "rio das ostras", "canário", "eucariontes", "vaso"]
substring = "rio"

# find() -> se não encontrar retorna -1

#for string in lista_strings:
#    posicao = string.find(substring)
#    if posicao != -1:
#        print(f"'{string}'")

for string in lista_strings:
    if "rio" in string:
        print(string)