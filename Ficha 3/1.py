import numpy as np
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
        aux[int(a)] = 1
    if (jog == "MIN"):
        aux[int(a)] = -1    
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
        v = 10
        for a in acoes(T):
            v1,ac,es = alfabeta(resultado(T,a,'MIN'),alfa,beta,'MAX')
            if v1 < v: # guardo a ação que corresponde ao pior
                v = v1
                ba = a
            beta = min(beta,v)
            if alfa>= beta:
                break
        return v,ba,resultado(T,ba,'MIN')

# ------------------------------------------------------------------
def joga_max(T):
    v,a,e = alfabeta(T,-10,10,'MAX')
    print ('MAX joga para ',int(a))
    return e

# ------------------------------------------------------------------
def joga_min(T):
    v,a,e = alfabeta(T,-10,10,'MIN')
    print ('MIN joga para ',int(a))
    return e

# ------------------------------------------------------------------
def jogo(T, p1,p2):
    # cria tabuleiro vazio
    #T = [0,0,0,0,0,0,0,0,0]
    # podemos partir de um estado mais "avançado"
    #T = [1,-1,0,0,-1,0,1,0,0]
    mostra_tabuleiro(T)
    while not estado_terminal(T):
        if p1.__name__ == "joga_rand" and p2.__name__ == "joga_min":
            T = p1(T, 1)
        elif p1.__name__ == "joga_rand" and p2.__name__ == "joga_max":
            T = p1(T, -1)
        else:
            T = p1(T)
        mostra_tabuleiro(T)
        if not estado_terminal(T):
            if p2.__name__ == "joga_rand" and p1.__name__ == "joga_min":
                T = p2(T, 1)
            elif p2.__name__ == "joga_rand" and p1.__name__ == "joga_max":
                T = p2(T, -1)
            else:    
                T = p2(T)
            mostra_tabuleiro(T)
    # fim
    if utilidade(T) == 1:
        print ('Venceu o MAX')
    elif utilidade(T) == -1:
        print ('Venceu o MIN')
    else:
        print ('Empate')

# ------------------------------------------------------------------
#dado um tabuleiro diz qual o proximo jogador a jogar, para uso no RAND
def descobreJogador(T):
    min = 0
    max = 0
    for a in T:
        if T[a] == -1:
            min = min + 1
        if T[a] == 1:
            max = max + 1
    if min > max:
        return 1
    if max > min:
        return -1
    if max == min:
        return -1

# jogador aleatório
def joga_rand(T, jog):
    #jog = descobreJogador(T)
    x = -1
    while(x not in acoes(T)):
        x = random.randint(0,8)
    T[x] = jog
    print (jog, ' joga para ',int(x))
    if jog == -1:
        return resultado(T,x,'MIN')
    if jog == 1:
        return resultado(T,x,'MAX')

# ------------------------------------------------------------------
# main
def main():
    # cria tabuleiro vazio
    T = [0,0,0,0,0,0,0,0,0]
    # deve ganhar quase sempre o max:
    jogo(T,joga_min, joga_rand)
    # devem empatar sempre:
    #jogo(T, joga_max,joga_min)


main()