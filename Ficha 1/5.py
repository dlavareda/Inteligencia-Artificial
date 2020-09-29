"""
A biblioteca numpy é muito útil para processamento matemático de dados
(tipo matlab). Para a podermos usar devemos fazer o seguinte import:
import numpy as np
Agora podemos criar, por exemplo, um array 7x3 (7 linhas e 3 colunas)
inicializado a zero com:
a = np.zeros([7,3])
Escreva um programa um programa que peça ao utilizador duas matrizes
quadradas 2x2, A e B, e mostre no ecrã:
(a) o produto elemento a elemento A.B
(b) o produto matricial A ∗ B
(c) a diferença entre matrizes A − B
(d) o logaritmo dos elementos de A (se existirem elementos negativos, use
o seu valor absoluto)
(e) o maior valor da segunda linha de A vezes o menor valor da primeira
coluna de B.
"""
import numpy as np


def lerMatriz():
    matriz = np.zeros([2, 2])
    for i in range(2):
        for j in range(2):
            print("Posição " + str(i) + " x " + str(j))
            matriz[i, j] = int(input())
    return matriz

def produtoElementoaElementoMatriz(a, b):
    z = a * b
    return z

def diferencaMatriz(a, b):
    z = a - b
    return z

def multiplicacaoMatriz(a, b):
    z = a.dot(b)
    return z

def logMatriz(a):
    a = np.absolute(a)
    z = np.log(a)
    return z

matriz1 = lerMatriz()
#matriz2 = lerMatriz()

z = logMatriz(matriz1)

print(z)