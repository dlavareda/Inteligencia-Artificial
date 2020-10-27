"""
Gerar mundos
Verificar se sao válidos so é valido de [3,1] + [1,3] ou [2,2]
Incrementar contadotes n de mundos validos, numero de poços em 3,1 ; 2,2 e 1,3

Exemplos 100000
Mundos válidos =  100000
Tentativas =  773999
P13  0.30547
P22  0.89226
P31  0.28716
            
Mundos válidos =  10000
Tentativas =  100332104
P13  0.9906
P22  0.9999
P31  0.9892
--- 2275.2772674560547 seconds ---

+------------+--------+--------+--------+-----------+
| Prob. poço |  [1,3] |  [2,2] |  [3,1] | Tempo [s] |
|    0.01    | 0.0204 | 0.9898 | 0.2931 |  16.173   |
|    0.20    | 0.3088 | 0.8925 | 0.2844 |   1.4502  |
|    0.50    | 0.5718 | 0.9131 | 0.5415 |   1.6587  |
|    0.80    | 0.8074 | 0.9785 | 0.7991 |   6.7948  |
|    0.99    | 0.9906 | 0.9999 | 0.9892 | 2275.2773 |
+------------+--------+--------+--------+-----------+
"""
import numpy as np
import time

def mostrarMundo(T):
    for l in range(0, 4):
        for c in range(0, 4):
            print(T[l][c] , end =" ")
        print()


def gerarMundo(T):
    for l in range(0, 4):
        for c in range(0, 4):
            #geração de poços
            if np.random.rand() <= 0.99:
                T[l][c] = 1
    T = gerarBrisas(T)
    return T

def gerarBrisas(T):
    for l in range(0, 4):
        for c in range(0, 4):
            if T[l][c] == 1:
                if l - 1 >= 0:
                    T[l-1][c] = 2
                if l + 1 < 4:
                    T[l+1][c] = 2
                if c - 1 >= 0:
                    T[l][c-1] = 2
                if c + 1 < 4:
                    T[l][c+1] = 2
    return T

def validaMundo(T):
    if T[3][0] == 0 and T[2][0] == 2 and T[3][1] == 2 :
        #print("Mundo Válido")
        return 1
    else:
        #print("Mundo Inválido")
        return 0 

def limparMundo(T):
    T = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    return T

def contaPocos(T):
    T10 = 0
    T21 = 0
    T32 = 0
    if T[1][0] == 1:
        T10 = 1
    if T[2][1] == 1:
        T21 = 1
    if T[3][2] == 1:
        T32 = 1
    return T10, T21, T32

def main():
    #guarda o numero de mundos válidos
    validos = 0
    #guarda o numero de vezes que foram necessárias para chegar ao numero de mundos validos
    i = 0
    T = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    PC13 = 0
    PC22 = 0
    PC31 = 0
    while(validos < 10000):
        i = i + 1
        T = gerarMundo(T)
        if validaMundo(T) == 1:
            validos += 1
            PC13tmp , PC22tmp , PC31tmp = contaPocos(T)
            PC13 = PC13 + PC13tmp
            PC22 = PC22 + PC22tmp
            PC31 = PC31 + PC31tmp

        T = limparMundo(T)

    print("Mundos válidos = ", validos)
    print("Tentativas = ", i)
    print("P13 ", PC13/validos)
    print("P22 ", PC22/validos)
    print("P31 ", PC31/validos)

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))