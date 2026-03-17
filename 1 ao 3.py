import random

lista_aleatoria=[]
for i in range(10):
    aleatorio=random.randint(1,20)
    lista_aleatoria.append(aleatorio)
print(lista_aleatoria)
#
#
def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i]==alvo:
            return i
    return -1

pos=busca_sequencial(lista_aleatoria, 7)
if pos!=-1:
    print("indice na lista:", pos)
else:
    print("não está na lista")
#
#
def contador_ocorrencias(lista, alvo):
    contador=0
    for i in lista:
        if i==alvo:
            contador+=1
    return contador
ocorrencias=contador_ocorrencias(lista_aleatoria, 4)
print("O número aparece", ocorrencias, "Vez(es)")
#
#
def menor_indice(lista):
    indice_menor=0
    for i in range(1,len(lista)):
        if lista[i]<lista[indice_menor]:
            indice_menor=i
    return indice_menor
indice_menor_resultado=menor_indice(lista_aleatoria)
print(lista_aleatoria[indice_menor_resultado])
