import networkx as nx

def V(graph):
    return set(graph.nodes())

def E(graph):
    return set(graph.edges())

def prims_initialize(graph, v ):
    if(v not in V(graph)):
        return 'Error: Vertex NOT Found'
    else:
        T=nx.Graph()
        T.add_node(v)
        return T

def is_spanning(graph, subgraph):
    return V(graph)==V(subgraph)

def cost(G, e):
    return G[e[0]][e[1]]['weight']

def possible_edges(G,T):
    return [e for e in list(G.edges(V(T))) if e[0] not in V(T) or e[1] not in V(T)]

def min_prims_edge(G,T):
    possible = possible_edges(G, T)
    minimum = 9999999999 #used to check for minimum default set to a really high num
    next_edge = list() #used to hold the edge that has the minimum weight
    for x in range(0,len(possible),1): #runs through the list of edges
        weight = cost(G,possible[x]) #keeps track of the weight
        print(weight)
        if weight < minimum: #compare the weight of the edge to current min
            minimum = cost(G,possible[x]) #set the min to the smallest weight
            next_edge = possible[x] #save the edge with small weight
    return next_edge #return the smallest edge