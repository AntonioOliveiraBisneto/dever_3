nomes = ["Alonso", "antonio", "Tiago", "jose carlos", "Eduardo", "Chris", "leticia"]
def busca_nome(lista, alvo):
    for i in range(len(lista)):
        if lista[i].lower()==alvo.lower():
            return i
    return -1
pos=busca_nome(nomes, "Antonio")
if pos!=-1:
    print("posição:", pos)
else:
    print("Nao ta ai não")