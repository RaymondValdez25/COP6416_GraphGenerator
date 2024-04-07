import numpy as np
import networkx as nx
import sys

def graphGenerator(n, k):
    np.set_printoptions(threshold=sys.maxsize)

    #generate a graph of n nodes
    #k = graph connected to the nearest k neighbors
    #p = probability of rewiring each edge
    G = nx.connected_watts_strogatz_graph(n, k, p=0.1)

    #n=100, k=10, p=0.1

    # Add random weights to the edges
    for (u, v) in G.edges():
        G[u][v]['weight'] = np.random.randint(1, 500)

    # Get the adjacency matrix
    adj_matrix = nx.adjacency_matrix(G).todense()

    # Print the adjacency matrix with proper format
    #print(np.array2string(adj_matrix, separator=','))

    # Return the matrix for use in data_analysis.py
    return(np.array(adj_matrix))
