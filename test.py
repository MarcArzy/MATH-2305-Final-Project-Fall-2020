
import networkx as nx
import matplotlib as plt
from functions import *
graph_data = open('G1.txt','r')

G = nx.read_weighted_edgelist(graph_data, nodetype = int)

T = prims_initialize(G, 4)
T.add_edge(2,4)
T.add_edge(1,3)
T.add_edge(2,3)
T.add_edge(4,5)
print(f'The vertex set of G is V(G) = {V(G)}')
print()
print(f'The edge set of G is E(G) = {E(G)}')
print()
print(f'is T spanning? {is_spanning(G,T)}')

def possible_edges(G,T):
    return [e for e in list(G.edges(V(T))) if e[0] not in V(T) or e[1] not in V(T)]

def min_prims_edge(G,T):
    possible = possible_edges(G, T)
    minimum = max
    for x in range(0,len(possible),1):
        if cost(G,possible[x]) < minimum:
            minimum = cost(G,possible[x])
    return minimum