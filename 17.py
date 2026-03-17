def contar_menores(lista, alvo):
    inicio=0
    fim=len(lista)
    while inicio<fim:
        meio=(inicio+fim)//2
        if lista[meio]<alvo:
            inicio=meio+1
        else:
            fim=meio
    return inicio
lista = [1, 2, 2, 4, 5, 7]
print(contar_menores(lista, 6))