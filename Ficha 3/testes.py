import numpy as np
import copy
import random

def mostra_tabuleiro(T):
    # IMPLEMENTAR
    for i in range(0, 9):
        if T[i] == -1:
            print("O", end =" ")
        elif T[i] == 1:
            print("X", end =" ")
        else:
            print(".", end =" ")
        if i == 2 or i == 5:
            print("")
    print("")

def acoes(T):
    # IMPLEMENTAR
    A = np.array([])
    for i in range(0, 9):
        if T[i] == 0:
            A = np.append(A, i)
    return A

#jog = MAX ou MIN
def resultado(T,a,jog):
    aux = copy.copy(T)
    if (jog == "MAX"):
        aux[a] = 1
    if (jog == "MIN"):
        aux[a] = -1    
    return aux

def utilidade(T):
    # testa as linhas
    for i in (0,3,6):
        #ganha por linhas
        if T[i] == T[i+1]== T[i+2]:
            if T[i] != 0:
                return T[i]
            
    # testa as colunas
    for i in (0,1,2):
            #ganha por Colunas
            if T[i] == T[i+3]== T[i+6]:
                if T[i] != 0:
                    return T[i]
    # testa as diagonais
    for i in (0,2):
        if (i == 0):
            if T[i] == T[i+4] == T[i+8]:
                return T[i]
        if (i == 2):
            if T[i] == T[i+2] == T[i+4]:
                return T[i]            

    # não é nodo folha ou dá empate
    return 0

# devolve True se T é terminal, senão devolve False
#Ainda ha espaço ou nao
def estado_terminal(T):
    for i in range(0, 8):
        if T[i] == 0:
            return False
    return True

def main():
    T = [0,0,0,0,0,0,0,0,0]
    mostra_tabuleiro(T)
    while(not estado_terminal(T) and utilidade(T) == 0):
        print("Jogada MIN")
        min = int(input())
        T = resultado(T, min, "MIN")
        mostra_tabuleiro(T)
        if (not estado_terminal(T) and utilidade(T)) != 0:
            break
        print("Jogada MAX")
        max = int(input())
        T = resultado(T, max, "MAX")
        mostra_tabuleiro(T)
        
    print("ganhou", utilidade(T))
main()