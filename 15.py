def busca_binaria_nome(lista, alvo):
    inicio=0
    fim=len(lista)-1
    alvo=alvo.lower()
    while inicio<=fim:
        meio=(inicio+fim)//2
        nome_meio=lista[meio].lower()
        if nome_meio==alvo:
            return meio
        elif nome_meio<alvo:
            inicio=meio+1
        else:
            fim=meio-1
    return -1
nomes = ["alonso", "Antonio", "Eduardo", "leticia", "Tiago"]
print(busca_binaria_nome(nomes, "eduardo"))