from functions import *
from drawing import *
import networkx as nx

graph_data = open('G1.txt','r')

G = nx.read_weighted_edgelist(graph_data, nodetype = int)

def prims_algorithm(G, starting_vertex):
    T = prims_initialize(G, starting_vertex)
    while is_spanning(G,T)==False:
        e = min_prims_edge(G,T)
        T.add_edge(e[0],e[1])
    return T

something = prims_algorithm(G, 4)

show_weighted_graph(G)
draw_subtree(G,something)
