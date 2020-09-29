"""
4 Veja como lidar com listas aqui.
Escreva um programa que tenha uma função que leia uma lista de inteiros
positivos do teclado (termine a leitura com a introdução de um número negativo);

outra função que receba 2 listas e mostre no ecrã os números que
aparecem em ambas as listas.

Agora escreva o programa para ler duas listas
do teclado e mostrar os elementos que são membros de ambas as listas (a
interseção das listas).
"""
#le lista de inteiros positivos até que o numero recebido seja negativo
def lerListaInteiros():
    lista = []
    numero = int(input())
    while numero > 0:
        lista.append(numero)
        numero = int(input())
    return lista


def comumListas(lista1, lista2):
    for i in lista1:
        if i in lista2:
            print(i)

print("Introduza a primeira lista")
list1 = lerListaInteiros()
print("Introduza a segunda lista")
list2 = lerListaInteiros()
print("Os elementos comuns são:")
comumListas(list1, list2)