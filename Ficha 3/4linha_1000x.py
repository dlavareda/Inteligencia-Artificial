#
import copy
import random
import sys
import time


def movimento(T, pos):
    if(pos == 0):
        if(T[8] == 0):
            return 8
        else:
            if(T[4] == 0):
                return 4
            else:
                return 0
    if(pos == 1):
        if(T[9] == 0):
            return 9
        else:
            if(T[5] == 0):
                return 5
            else:
                return 1
    if(pos == 2):
        if(T[10] == 0):
            return 10
        else:
            if(T[6] == 0):
                return 6
            else:
                return 2
    if(pos == 3):
        if(T[11] == 0):
            return 11
        else:
            if(T[7] == 0):
                return 7
            else:
                return 3


# ------------------------------------------------------------------
def mostra_tabuleiro(T):
    print("\n")
    for i in [0, 4, 8]:
        for j in range(0, 4, 1):
            if(T[i+j] == 1):
                print(" X ", end='')
            elif(T[i+j] == -1):
                print(" O ", end='')
            else:
                print(" . ", end='')
        print("\n")


# ------------------------------------------------------------------
# devolve a lista de ações que se podem executar partido de um estado
def acoes(T):
    actions = []
    for i in range(0, 4):
        y = movimento(T, i)
        if(T[y] == 0):
            actions.append(y)
        actions = list(dict.fromkeys(actions))
    return actions

# ------------------------------------------------------------------
# devolve o estado que resulta de partir de um estado e executar uma ação


def resultado(T, a, jog):
    aux = copy.copy(T)
    if(jog == "MAX"):
        aux[a] = 1
    else:
        aux[a] = -1
    return aux

# ------------------------------------------------------------------
# existem 8 possíveis alinhamentos vencedores, para cada jogador


def utilidade(T):
    # testa as linhas
    for i in [0, 4, 8]:
        if(T[i] == 1 and T[i+1] == 1 and T[i+2] == 1):
            return 1
        if(T[i+1] == 1 and T[i+2] == 1 and T[i+3] == 1):
            return 1
        if(T[i] == -1 and T[i+1] == -1 and T[i+2] == -1):
            return -1
        if(T[i+1] == -1 and T[i+2] == -1 and T[i+3] == -1):
            return -1
    # testa as colunas
    for i in range(0, 4):
        if(T[i] == 1 and T[i+4] == 1 and T[i+8] == 1):
            return 1
        if(T[i] == -1 and T[i+4] == -1 and T[i+8] == -1):
            return -1
    # testa as diagonais
    if(T[0] == 1 and T[5] == 1 and T[10] == 1):
        return 1
    if(T[1] == 1 and T[6] == 1 and T[11] == 1):
        return 1
    if(T[3] == 1 and T[6] == 1 and T[9] == 1):
        return 1
    if(T[2] == 1 and T[4] == 1 and T[9] == 1):
        return 1
    if(T[0] == -1 and T[5] == -1 and T[10] == -1):
        return -1
    if(T[1] == -1 and T[6] == -1 and T[11] == -1):
        return -1
    if(T[3] == -1 and T[6] == -1 and T[9] == -1):
        return -1
    if(T[2] == -1 and T[4] == -1 and T[9] == -1):
        return -1
    # não é nodo folha ou dá empate
    return 0

# ------------------------------------------------------------------
# devolve True se T é terminal, senão devolve False


def estado_terminal(T):
    final = utilidade(T)
    if (final == 1 or final == -1):
        return True
    for i in range(0, 12):
        if(T[i] == 0):
            return False
    return True


# ------------------------------------------------------------------
# algoritmo da wikipedia
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
# ignoramos a profundidade e devolvemos o valor, a ação e o estado resultante
def alfabeta(T, alfa, beta, jog):
    if estado_terminal(T):
        return utilidade(T), -1, -1
    if jog:
        v = -10
        ba = -1
        for a in acoes(T):
            v1, ac, es = alfabeta(resultado(T, a, 'MAX'), alfa, beta, False)
            if v1 > v:  # guardo a ação que corresponde ao melhor
                v = v1
                ba = a
            alfa = max(alfa, v)
            if beta <= alfa:
                break
        return v, ba, resultado(T, ba, 'MAX')
    else:
        v = 10
        ba = 1
        for a in acoes(T):
            v1, ac, es = alfabeta(resultado(T, a, 'MIN'), alfa, beta, True)
            if v1 < v:
                v = v1
                ba = a
            beta = min(beta, v)
            if beta <= alfa:
                break
        return v, ba, resultado(T, ba, 'MIN')

# ------------------------------------------------------------------


def joga_max(T):
    v, a, e = alfabeta(T, -10, 10, True)
    print("MAX joga para ", a)
    return e

# ------------------------------------------------------------------


def joga_min(T):
    v, a, e = alfabeta(T, -10, 10, False)
    print("MIN joga para ", a)
    return e

# ------------------------------------------------------------------


def jogo(p1,p2):
	# cria tabuleiro vazio
	T = [0,0,0,0,0,0,0,0,0,0,0,0]
	# podemos partir de um estado mais "avançado"
	#T = [1,-1,0,0,-1,0,1,0,0]
	mostra_tabuleiro(T)
	while acoes(T) != [] and not estado_terminal(T):
		T=p1(T)
		mostra_tabuleiro(T)
		if acoes(T) != [] and not estado_terminal(T):
			T=p2(T)
			mostra_tabuleiro(T)
	# fim
	if utilidade(T) == 1:
		print ('Venceu o rand')
		return 1
	elif utilidade(T) == -1:
		print ('Venceu o min')
		return -1
	else:
		print ('Empate')
		return 0

# ------------------------------------------------------------------

# jogador aleatório


def joga_rand(T):
    x = random.randint(0, 3)
    y = movimento(T, x)
    T[y] = 1

    print("RAND joga para ", y)
    return T


def joga_humano(T):
    x = int(input("Introduza a jogada"))
    while(x < 0 or x > 3):
        x = int(input("Introduza a jogada"))
    y = movimento(T, x)
    T[y] = -1

    print("JOG joga para ", y)
    return T

# ------------------------------------------------------------------
# main


# deve ganhar sempre o max:
# jogo(joga_max,joga_rand)
# jogo(joga_max,joga_humano)
# devem empatar sempre:
start_time = time.time()


count_max = 0
count_min = 0
count_empate = 0
for x in range(10000):
    res = jogo(joga_min, joga_rand)
    if res == 1:
        count_max = count_max + 1
    if res == -1:
        count_min = count_min + 1
    if res == 0:
        count_empate = count_empate + 1
print("Vitorias rand ", count_max)
print("Vitorias min ", count_min)
print("Empates ", count_empate)
print("--- %s seconds ---" % (time.time() - start_time))
