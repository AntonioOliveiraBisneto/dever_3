def busca_matriz(matriz, alvo):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==alvo:
                return (i, j)
    return (-1, -1)
matriz=[
    [1, 8, 2],
    [7, 3, 4],
    [9, 5, 6]
]
alvo=7
posicao = busca_matriz(matriz, alvo)
if posicao != (-1, -1):
    print("Número encontrado na posição:", posicao)
else:
    print("Número não encontrado")