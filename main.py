import networkx as nx
from functions import * 
from drawing import *
from algorithms import *

graph_data = open('test-graphs/G4.txt','r') #read in the graph you want to test G1-G4

G = nx.read_weighted_edgelist(graph_data, nodetype = int) #create initial graph 

T = prims_algorithm(G, int(input("Type starting vertex: ")), True, True) #ask the user what verticy they want to start on

