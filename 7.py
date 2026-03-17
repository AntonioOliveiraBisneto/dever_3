import random
lista=[]
for i in range(50):
    lista.append(random.randint(1,75))
print(lista)

def busca_50(lista):
    for i in range(len(lista)):
        if lista[i] > 50:
            return (i, lista[i])
    return (-1, -1)
resultado=busca_50(lista)
if resultado!=(-1, -1):
    print("indice:", resultado[0], "calor:", resultado[1])
else:
    print("nenhum numero maior que 50.")