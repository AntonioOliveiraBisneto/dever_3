def busca_18(lista):
    for aluno in lista:
        if aluno["idade"]>=18:
            return aluno["nome"]
    return None
alunos=[
    {"nome": "alonso", "idade":17},
    {"nome": "antonio", "idade":17},
    {"nome": "eduardo", "idade":19},
    {"nome": "jose carlos", "idade":18},
    {"nome": "leticia", "idade":21},
]
resultado_18=busca_18(alunos)
if resultado_18:
    print("Primeiro maior de 18:", (resultado_18))
else:
    print("todos são menores de idade")