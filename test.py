'''
import networkx as nx
from functions import *
from algorithms import prims_algorithm
from drawing import *
'''
import networkx as nx
from functions import *
from algorithms import prims_algorithm
from drawing import *


graph_data = open('test-graphs/G1.txt', 'r')
'''
will open and return a file object from test-graphs folder in this case a graph to be read,
if file is not found will raise an error
'''
G=nx.read_weighted_edgelist(graph_data, nodetype=int)
'''
NetworkX will then generate a plot for the chosen file
and will ensure returning a hashable type
'''
T= prims_algorithm(G, 0, show_graph = True, show_cost = True)
'''
Will then run with 0 as the starting vertex
'''
