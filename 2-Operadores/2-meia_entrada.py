# Solicitando idade e se é estudante
idade = int(input('Digite sua idade: '))
estudante = input(" Você é estudante s/n: ") 

meia = (idade >= 60) or estudante == "s"

# Apresentando o resultado ao usuário
print("Tem direto a meia-entrada", meia)