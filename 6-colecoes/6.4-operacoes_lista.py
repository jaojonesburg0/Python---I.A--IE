lista_inicial = ["João","Pamela","Dominique"]
print("lista inicial: " ,lista_inicial)
print(60 * "-")
#===========Acrescentando append========================================
lista_inicial.append("Eduarda")
print("Após o append()", lista_inicial)
print(60 * "-")
#===========Acrescentando item em posição específica====================
lista_inicial.insert(2,"Matheus")
print("Após o insert()", lista_inicial)
print(60 * "-")
#===========Modificando item em uma lista==============================
lista_inicial[3] = "Rafael"
print("Após a modificação: ", lista_inicial)
print(60 * "-")
#===========Apagando item em índice específico=========================
del lista_inicial[3]
print("Após del: ", lista_inicial)
print(60 * "-")
#===========Apagando valor específico==================================
lista_inicial.remove("Pamela")
print("Após remove: ", lista_inicial)
print(60 * "-")
#===========Apagando e Armazenando valor da lista======================
removido = lista_inicial.pop(1)
print(f"Após pop, removido {removido}", lista_inicial)
print(60 * "-")
#===========LImpando completamente lista==============================
lista_inicial.clear()
print("Após clear: ")