import networkx as nx

"""
This is functions
-----------------

The function Document is used to hold all the code used to make the prims algorithm function in the algorithm Document
We import "networkx" in this document so that we can peek into the graphs vertices and their edges
"""

def V(graph):
    """
    Parameters
    ---------
    takes in read in graph information from text documents called from main.py
    
    function
    --------
    This functions calls the nodes function from networkx to create a list of vertices for our graph
    """
    return set(graph.nodes()) #list of vertices

def E(graph):
    """
    Parameters
    ----------
    takes in read in graph information from text documents called from main.py
    
    function
    --------
    This functions calls the nodes function from networkx to create a list of edges for our graph
    """
    return set(graph.edges()) #list of edges

def prims_initialize(graph, v ): #checks if the starting verticy exists
    """
    Parameters
    ----------
    graph = list
    v = starting verticy of the subtree
    
    function
    --------
    This function helps helps us catch any verticy errors if the user enters or searches for a 
    starting verticy that doesn't exist in the graph. If the verticy exists it will execute the ''else'' statement
    returning a subgraph starting at the requested verticy, but if it doesn't exist, then it executes the ''if'' statement 
    returning an error message.
    """
    if(v not in V(graph)):
        return 'Error: Vertex NOT Found' #error message
    else: #initializes the subtree
        T=nx.Graph()
        T.add_node(v)
        return T

def is_spanning(graph, subgraph): # makes sure the subtree doesn't include cycles or all edges of G
    """
    Parameters
    ----------
    graph = original graph/ reference graph
    subgraph = subtree of original graph. this is the minimum spanning tree
    
    function
    --------
    This function is to help us find out if the subtree is spanning. When we say spanning, it means that the subtree
    is able to contain all the vertices from the parent graph without holding all the same edges. If the subtree matches
    the same vertices with it's parent graph the this function will return false. This is used as a limiter in
    the algorithm's while loop
    """
    return V(graph)==V(subgraph)

def cost(G, e): #return the weight of the edge
    """
    Parameters
    ----------
    G = the graph with weights
    e = the tuple of vertices that make the edge
   
    function
    ---------
    This function is used to help us find the cost of an edge. It takes the the two vertices that create the edge
    G[0][1] and then calls for the ['weight']. This function is used to help us measure the weights of the edges.
    """
    return G[e[0]][e[1]]['weight']

def possible_edges(G,T): #checks to see what edges don't create a cycle
    """
    Parameters
    ----------
    G = original graph
    T = subtree, prims minimum spanning tree
    
    function
    --------
    This function gives us a list of edges that follow prims rule of not creating cycles. This checks and returns vertices that do not connect to
    already virticies
    """
    return [e for e in list(G.edges(V(T))) if e[0] not in V(T) or e[1] not in V(T)]

def min_prims_edge(G,T):
    """
    Parameters
    ---------
    G = original tree
    T = subtree, prims minimum spanning tree
    
    function
    --------
    this function goes through all the possible edges and checks their weights. if the weight is less than the current minimum hold
    then it replaces the current minimum variable and returns it to the algorithm function in algorithms.py
    """
    possible = possible_edges(G, T)
    minimum = 9999999999 #used to check for minimum default set to a really high num
    next_edge = list() #used to hold the edge that has the minimum weight
    for x in range(0,len(possible),1): #runs through the list of edges
        weight = cost(G,possible[x]) #keeps track of the weight
        if weight < minimum: #compare the weight of the edge to current min
            minimum = cost(G,possible[x]) #set the min to the smallest weight
            next_edge = possible[x] #save the edge with small weight
    return next_edge #return the smallest edge
