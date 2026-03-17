def primeiro(lista, alvo):
    inicio=0
    fim = len(lista)-1
    resultado=-1
    while inicio<=fim:
        meio=(inicio+fim)//2
        if lista[meio]==alvo:
            resultado=meio
            fim=meio-1
        elif lista[meio]<alvo:
            inicio=meio+1
        else:
            fim=meio-1
    return resultado
lista = [1, 2, 2, 4, 4]
print(primeiro(lista, 4))

##

def ultimo(lista, alvo):
    inicio=0
    fim=len(lista)-1
    resultado=-1
    while inicio<=fim:
        meio=(inicio+fim)//2
        if lista[meio]==alvo:
            resultado=meio
            inicio=meio+1
        elif lista[meio]<alvo:
            inicio=meio+1
        else:
            fim=meio-1
    return resultado
print(ultimo(lista, 4))