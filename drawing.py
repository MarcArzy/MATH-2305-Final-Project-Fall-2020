"""Drawing.py description

This script allows for the drawing and showing of both our weighted graphs and theire subtrees. 

This script requires the importation of the packages `matplotlib`, 'NumPy', and 'networkx' within the Python
environment you are running this script in.

This script contains the following
functions:

    * show_weighted_graph- shows our weighted graph 
    * draw_subtree - drawing  and showing the weighted graph's corresponding subtree
"""
import networkx as nx    ## import NetworkX to create our network attributes
import matplotlib.pyplot as plt   ## inport matplotlib to plot our subtree and weighted graph
import numpy as np             ### import NumPy for arraw manipulations

def show_weighted_graph(G):
    """ creates and shows the weightwed graph

    Parameters
    ----------
    G : NetworkX graph or list of nodes
    pos : A dictionary of positions keyed by node

    Returns
    -------
    The weighted graph
    """
    pos = nx.planar_layout(G)             ## assigning position of G's nodes to "pos"
    nx.draw(G, pos)                    ## draws the graph G with respective layout 
    labels = nx.get_edge_attributes(G,'weight')   ## gets edge weight    
    nx.draw_networkx_edge_labels(G,                  ## drawing weighted graph's edge labels using layout 
                                 pos,           
                                 edge_labels = labels)
    plt.show()                               ## shows plot
    
def draw_subtree(G,T):
    """ creates and shows the weightwed graph

    Parameters
    ----------
    G : NetworkX graph or list of nodes
    T = Subtree, gets edge attributes

    Returns
    -------
    The corresponding subtree of the weighted graph
    """
    pos = nx.planar_layout(G) ## 
    nx.draw_networkx(G,pos)   
    labels = nx.labels = nx.get_edge_attributes(G,'weight') 
    nx.draw_networkx_edge_labels(G,                  
                                 pos,           ## Creates edge labels for subtree using graph layout, position and weights
                                 edge_labels = labels)
    nx.draw_networkx_edges(G, 
                           pos, 
                           edgelist=T.edges(),   #### Draws tree's edges using graph layout
                           width=8, alpha=0.5,     ### and assigns other attributes (e.g. color, width) to network edges
                           edge_color='r')
    nx.draw_networkx_nodes(G, 
                           pos,                 ### Draws tree's nodes using layout 
                           nodelist=T.nodes(),   ## and ssigns other attributes (e.g. size, color) to network nodes
                           node_size=500, 
                           alpha=0.5, 
                           node_color='r')
    plt.show()                                  ## shows plot
