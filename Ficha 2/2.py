"""2. Modifique o programa anterior para que a pesquisa seja efetuada usando um
método informado: a pesquisa A∗
. Comece por definir a heurística a usar.
"""
import csv
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
from networkx import algorithms

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
    #Leira da origem e destino
    origem = ""
    while not G.has_node(origem):
        print("Qual a cidade de origem?")
        origem = input()
    destino = ""
    while not G.has_node(destino):
        print("Qual a cidade de destino?")
        destino = input()
    #Gera o caminho
    caminho = nx.astar_path(G, origem, destino, weight='weight')
    #Mostra caminho e Distancia
    print(caminho, "- Distancia =", somaDistancia(G, caminho))

main()