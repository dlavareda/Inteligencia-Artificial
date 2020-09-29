"""
2. Escreva um programa que peça ao utilizador um número inteiro positivo
menor que 100 e mostre no ecrã quantas dezenas e quantas unidades tem o
número lido.
"""
print("Introduza um numero inteiro positivo menor que 100")
numero = int(input())
if numero < 100:
    print("Unidades = " + str(numero % 10))
    numero = numero // 10
    print("Dezenas = " + str(numero))
else:
    print("O numero nao é menor do que 100")
