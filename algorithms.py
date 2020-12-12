from functions import *
from drawing import *
import networkx as nx

def prims_algorithm(G, starting_vertex, show_graph, show_cost):
    
    T = prims_initialize(G, starting_vertex)
    
    if isinstance(T,str) == True: #checks if the vertex exists in the graph
        print(T)
        return T
        
    while is_spanning(G,T)==False: #check functions
        e = min_prims_edge(G,T)
        T.add_edge(e[0],e[1])
        
    if show_graph == True: #display a visual representation of the subtree
        show_weighted_graph(G)
        draw_subtree(G,T)
        
    if show_cost == True: #display the weight of the graph
        total_cost = 0
        for x in E(T): #add up all the weights
            total_cost = total_cost + cost(G,x)
        print(total_cost)
            
    return T

