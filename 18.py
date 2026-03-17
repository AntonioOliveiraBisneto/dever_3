def busca_binaria(linha, alvo):
    inicio=0
    fim=len(linha)-1
    while inicio<=fim:
        meio=(inicio+fim)//2
        if linha[meio]==alvo:
            return meio
        elif linha[meio]<alvo:
            inicio=meio+1
        else:
            fim=meio-1
    return -1
def busca_matriz_binaria(matriz, alvo):
    for i in range(len(matriz)):
        coluna=busca_binaria(matriz[i], alvo)
        if coluna!=-1:
            return (i, coluna)
    return (-1, -1)