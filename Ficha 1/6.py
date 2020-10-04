"""
6. O Python tem vários tipos de dados estruturados standard, entre os quais, as
listas, os dicionários e os conjuntos. Vejamos um exercício com dicionários:
escreva um programa que permita guardar a nota que obteve em várias UCs,
usando um dicionário. Deve ter um menu que permita: inserir um novo par
UC + nota, alterar o valor da nota duma UC, mostrar todos os pares UC +
nota e mostrar a nota média.
"""

notas = {}
resposta = 0
while int(resposta) < 4:
    print("#1 - Inserir")
    print("#2 - Alterar")
    print("#3 - Listar")
    print("#4 - Sair")
    resposta = input()
    if int(resposta) == 1:
        print("#### Inserir Nota ####")
        print("UC: ")
        uc = input()
        print("Nota: ")
        nota = input()
        notas[uc] = nota
    if int(resposta) == 2:
        print("#### Alterar Nota ####")
        print("UC: ")
        uc = input()
        if uc in notas:
            print("Nota: ")
            nota = input()
            notas[uc] = nota
        else:
            print("!!!! UC não encontrada !!!!")
    if int(resposta) == 3:
        if len(notas) > 0:
            print("#### Listar Notas ####")
            print(notas)
            print()
            print("#### Nota Média ####")
            i = 0
            sum = 0
            for nota in notas.values():
                i = int(i) + 1
                sum += int(nota)
            print("Média = " + str(sum/int(i)))
        else:
            print("!!!! Lista Vazia !!!!")
