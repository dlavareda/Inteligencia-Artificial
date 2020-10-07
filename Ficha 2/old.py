"""
Para trabalharmos com grafos vamos importar a seguinte biblioteca:
import networkx as nx
Agora escreva um programa que use a referida biblioteca para representar
as principais ligações rodoviárias entre as 18 capitais de distrito de Portugal
continental tal como apresentadas na Figura 1.
O seu programa deverá listar para cada cidade do mapa o conjunto das suas
cidades vizinhas (aquelas que se podem alcançar sem passar por nenhuma
outra cidade).
Sugestões:
-Comece por ver o simples tutorial que aparece no site da networkx em
https://networkx.github.io/documentation/stable.
- Represente num ficheiro de texto cada ligação (aresta do grafo) numa linha
com o seguinte formato: ORIGEM,DESTINO,DISTÂNCIA. Não coloque
espaços entre as vírgulas. Exemplo: AV,VI,100.
- Use a biblioteca CSV para ler do ficheiro: https://docs.python.
org/3/library/csv.html
- Carregue, a partir do ficheiro de texto, cada aresta e adicione a um grafo
"""

import csv
import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
nx.draw(G)

with open('/home/dlavareda/Documents/UBI/IA/Inteligencia-Artificial/Ficha 1/mapa.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        G.add_edge(row[0], row[1], weight=row[2])


print("Qual a cidade de origem?")
origem = input()

print("Qual a cidade de destino?")
destino = input()

sp = dict(nx.all_pairs_shortest_path(G))
caminho = sp[origem][destino]
print(caminho)




print("Deseja ver o mapa? 1-SIM 0-NAO")
resp = input()
if int(resp) == 1:
    plt.figure(3,figsize=(18,18)) 
    pos = nx.spring_layout(G)
    nx.draw_networkx(G,pos)
    # draw path in red
    path = nx.shortest_path(G, source=origem, target=destino)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    #guarda imagem
    plt.savefig("Ficha 2/map.png")
    #mostra imagem
    plt.show()

"""
print("Deseja ver o mapa? 1-SIM 0-NAO")
resp = input()
if int(resp) == 1:
    plt.figure(3,figsize=(18,18)) 
    pos = nx.spring_layout(G)
    nx.draw_networkx(G,pos)
    # draw path in red
    path = nx.shortest_path(G, source=origem, target=destino)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    #guarda imagem
    plt.savefig("Ficha 2/map.png")
    #mostra imagem
    plt.show()
"""