"""
1. Escreva um programa que mostre no ecrã os números ímpares entre 10 e 34
(tire partido da função range() e verá que só usa 2 linhas de código). Modifique o programa para que os números ímpares apareçam todos na mesma
linha.
"""

for i in range(10,34):
    if i%2 == 1:
        #print (i)
        print (i, end=' ')