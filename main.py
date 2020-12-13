'''
import networkx as nx
from functions import * 
from drawing import *
from algorithms import *
'''
import networkx as nx
from functions import * 
from drawing import *
from algorithms import *


graph_data = open('test-graphs/G1.txt','r') #read in the graph you want to test G1-G4
'''
will open and return a file object from test-graphs folder in this case a graph to be read,
if file is not found will raise an error
'''
G = nx.read_weighted_edgelist(graph_data, nodetype = int) #create initial graph 
'''
NetworkX will then generate a plot for the chosen file
and will ensure returning a hashable type
'''
T = prims_algorithm(G, int(input("Type starting vertex: ")), True, True) #ask the user what verticy they want to start on
'''
Will then ask for an input for a starting vertex 
'''
