"""1. Adapte a sua solução do exercício 8 da folha 1 para que o seu programa
peça ao utilizador para introduzir uma cidade de partida e outra de destino e,
usando a pesquisa não informada primeiro em largura:
(a) mostre a solução obtida sob a forma da sequência de cidades correspondente ao caminho a percorrer entre a cidade de partida e a de destino;
(b) mostre o comprimento total do percurso a percorrer;
(c) mostre no ecrã a árvore de pesquisa criada pelo seu algoritmo ao procurar a solução.
"""

import csv
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx


#Leitura do ficheiro .txt e criação do Grafo
def readGraph():
    G = nx.Graph()
    with open('/home/dlavareda/Documents/UBI/IA/GITHUB/Inteligencia-Artificial/Ficha 1/mapa.txt', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            G.add_edge(row[0], row[1], weight=int(row[2]))
    return G

#Cálculo da distancia da viagem
def somaDistancia(G, L):
    sum = 0
    for i in range(0, len(L) - 1):
        start = L[i]
        end = L[i + 1]
        sum += int(G[start][end]['weight'])
    return sum

def main():
    G = readGraph()
    nx.draw(G)
    #Leira da origem e destino
    origem = ""
    while not G.has_node(origem):
        print("Qual a cidade de origem?")
        origem = input()
    destino = ""
    while not G.has_node(destino):
        print("Qual a cidade de destino?")
        destino = input()
    #Gera a Árvore
    tree = nx.traversal.breadth_first_search.bfs_tree(G, origem)
    #Gera o caminho
    caminho = nx.shortest_paths.generic.shortest_path(tree, origem, destino)
    #Mostra caminho e Distancia
    print(caminho, "- Distancia =", somaDistancia(G, caminho))
    #desenha grafo
    nx.draw(tree, with_labels=True)
    #guarda imagem
    plt.savefig("Ficha 2/map(1).png")
    #mostra imagem
    plt.show()

main()