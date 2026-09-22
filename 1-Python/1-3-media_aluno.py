# criando a variável nome e as variáveis notas
nome = input("Nota do Aluno:")
nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
nota_3 = float(input("Nota 3: "))

# calculando a média do aluno
media = (nota_1 + nota_2 + nota_3) / 3

# apresentando o resultado ao usuário
print("A média do aluno(a) ", nome, " é ", media)
