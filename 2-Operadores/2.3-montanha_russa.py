# Solicitando altura e idade para embarcar na montanha russa
altura = float(input("Digite sua altura: "))
idade = int(input("Digite sua idade: "))

# Checando autorização
autorizacao = (altura >= 1.40) and (idade >= 12)

if autorizacao:

    print("Tem autorização para embarcar na Montanha Russa")
else:
    print("Não tem autorização para embarcar na Montanha Russa")