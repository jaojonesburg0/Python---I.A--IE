# criando função
def maior_numero(x,y):
    if x > y:
        return x
    else:
        return y

# solicitando os 2 numeros ao usuario
numero_1 = float(input("Digite um número "))
numero_2 = float(input("Digite um número "))

# chamando a função para ver o resultado
resultado = maior_numero(numero_1,numero_2)

# apresentando o maior numero ao usuario
print(f"O maior resultado foi: {resultado}")