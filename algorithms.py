"""Algorithm File"""

from functions import *
from drawing import *
import networkx as nx

"""
    modules and imports
    -------------------
    Import functions from functions tab.
    Import fuctions from drawing tab.
    Import networkx as nx.
    
    This is an algorithm script file.
    First we initializes the starting vertex.
    Checking if the vertex is in the graph.
    Checking if spanning is False then add another minimum edge.
    Drawing subtree.
    Printing cost for spanning tree.
"""
    
def prims_algorithm(G, starting_vertex, show_graph, show_cost):
    
    T = prims_initialize(G, starting_vertex)
    """
    Checking the Vertex
    ------
    """
    if isinstance(T,str) == True: #checks if the vertex exists in the graph
        print(T)
        return T
    
        """
        Show graph G.
        -------
        """
        
    if show_graph == True: #display a visual representation of the subtree
            show_weighted_graph(G)
            
    """
    Checking if T is Spanning.
    -------
    """
          
    while is_spanning(G,T)==False: #check functions
        e = min_prims_edge(G,T)
        T.add_edge(e[0],e[1])
        if show_cost == True:
            print(cost(G,e))
        """
        Display subtree.
        ------
        """
        
        if show_graph == True: #display a visual representation of the subtree
            draw_subtree(G,T)
        
        """
        Show Cost
        --------
        """
    if show_cost == True: #display the weight of the graph
        total_cost = 0
        for x in E(T): #add up all the weights
            total_cost = total_cost + cost(G,x)
        print("The cost of the spanning tree is: " + str(total_cost))
        
    """
    Return Function
    -------
    """
    return T

