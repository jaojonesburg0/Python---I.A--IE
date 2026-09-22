# criando funções e utilizando operadores matematicos

def soma (a,b):
    return a + b
def subtrair(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    if b == 0:
        return "Erro divisão por 0 não é permitida"
    return a / b

# pedindo informações ao usuário
numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite um número: "))

# apresentando resultados das operações
print(soma(numero_1,numero_2))
print(subtrair(numero_1,numero_2))
print(multiplicar(numero_1,numero_2))
print(dividir(numero_1,numero_2))

print("Quatro operações completadas!")