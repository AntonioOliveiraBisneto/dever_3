def mais_proximo(lista, alvo):
    inicio=0
    fim=len(lista)-1
    while inicio<=fim:
        meio=(inicio+fim)//2
        if lista[meio]==alvo:
            return meio
        elif lista[meio]<alvo:
            inicio=meio+1
        else:
            fim=meio-1
    if inicio>=len(lista):
        return len(lista)-1
    if fim<0:
        return 0
    if abs(lista[inicio]-alvo)<abs(lista[fim]-alvo):
        return inicio
    else:
        return fim
lista=[2, 5, 8, 12, 16]
indice=mais_proximo(lista, 11)
print("Índice:", indice, "Valor:", lista[indice])