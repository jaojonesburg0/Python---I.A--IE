# solciitando dados ao cliente

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Verificando a faixa etaria do cliente
if idade == 0:
    faixa = "RN"
elif idade <= 3:
    faixa = "Bebê"
elif idade <= 10:
    faixa = "Criança"
elif idade <= 14:
    faixa = "Adolescente"
elif idade <= 30:
    faixa = "Jovem"
elif idade <= 64:
    faixa = "Adulto"
else:
    faixa = "Idoso"

print(f"{nome}, você tem {idade} anos e está na faixa: {faixa}.")