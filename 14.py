def indice(lista, alvo):
    inicio=0
    fim=len(lista)
    while inicio<fim:
        meio=(inicio+fim)//2
        if lista[meio]<alvo:
            inicio=meio+1
        else:
            fim=meio
    return inicio
lista = [1, 3, 5, 7]
print(indice(lista, 6))