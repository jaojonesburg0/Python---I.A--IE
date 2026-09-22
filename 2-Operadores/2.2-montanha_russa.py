# Solicitando altura e idade para embarcar na montanha russa
altura = float(input("Digite sua altura: "))
idade = int(input("Digite sua idade: "))

# Checando autorização
autorizacao = (altura >= 1.40) and (idade >= 12)
print("Permissão para andar na montanha-russa: ", autorizacao)