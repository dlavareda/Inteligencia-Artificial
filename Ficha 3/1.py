"""
Posição pode valer 1 se estiver ocupada pelo jogador MAX, -1 se estiver ocupada pelo jogador MIN e 0 se estiver vazia.

Tabuleiro
0 1 2
3 4 5
6 7 8

MAX joga para 0
X . .
. . .
. . .

O - MIN
X - MAX
. - Vazio

"""



# coding: utf8
import copy
import random

# ------------------------------------------------------------------
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

# ------------------------------------------------------------------
# devolve a lista de ações que se podem executar partido de um estado
#Cada numero representamudar uma peça para essa posição

def acoes(T):
    # IMPLEMENTAR
    A = np.array([])
    for i in range(0, 9):
        if T[i] == 0:
            A = np.append(A, i)
    return A

# ------------------------------------------------------------------
# devolve o estado que resulta de partir de um estado e executar uma ação
def resultado(T,a,jog):
    aux = copy.copy(T)
    if (jog == "MAX"):
        aux[a] = 1
    if (jog == "MIN"):
        aux[a] = -1    
    return aux

# ------------------------------------------------------------------
# existem 8 possíveis alinhamentos vencedores, para cada jogador
#1 se ganha MAX, -1 se ganha MIN, 0 se empatado ou faltam jogadas
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

# ------------------------------------------------------------------
# devolve True se T é terminal, senão devolve False
#Ainda ha espaço ou nao
def estado_terminal(T):
    for i in range(0, 8):
        if T[i] == 0:
            return False
    return True
# ------------------------------------------------------------------
# algoritmo da wikipedia
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
# ignoramos a profundidade e devolvemos o valor, a ação e o estado resultante
# So falta criar para o MIN
def alfabeta(T,alfa,beta,jog):
    if estado_terminal(T):
        return utilidade(T),-1,-1
    if jog == 'MAX':
        v = -10
        ba = -1
        for a in acoes(T):
            v1,ac,es = alfabeta(resultado(T,a,'MAX'),alfa,beta,'MIN')
            if v1 > v: # guardo a ação que corresponde ao melhor
                v = v1
                ba = a
            alfa = max(alfa,v)
            if beta <= alfa:
                break
        return v,ba,resultado(T,ba,'MAX')
    else:
        # COMPLETAR

# ------------------------------------------------------------------
def joga_max(T):
    v,a,e = alfabeta(T,-10,10,'MAX')
    print ('MAX joga para ',a)
    return e

# ------------------------------------------------------------------
def joga_min(T):
    # IMPLEMENTAR

# ------------------------------------------------------------------
def jogo(p1,p2):
    # cria tabuleiro vazio
    T = [0,0,0,0,0,0,0,0,0]
    # podemos partir de um estado mais "avançado"
    #T = [1,-1,0,0,-1,0,1,0,0]
    mostra_tabuleiro(T)
    while not estado_terminal(T):
        T = p1(T)
        mostra_tabuleiro(T)
        if not estado_terminal(T):
            T = p2(T)
            mostra_tabuleiro(T)
    # fim
    if utilidade(T) == 1:
        print ('Venceu o jog1')
    elif utilidade(T) == -1:
        print ('Venceu o jog2')
    else:
        print ('Empate')

# ------------------------------------------------------------------
# jogador aleatório
def joga_rand(T):
    x = random.randint(0,8)
    # COMPLETAR
    return T

# ------------------------------------------------------------------
# main
def main():
    # deve ganhar quase sempre o max:
    jogo(joga_max,joga_rand)
    # devem empatar sempre:
    #jogo(joga_max,joga_min)


main()