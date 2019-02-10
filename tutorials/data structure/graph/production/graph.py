#=========================================
# coding = utf-8
#=========================================
# Name         : graph.py 
# Author       : Anthony Rey
# Version      : 1.0.0.0
# Date         : 10/02/2019
# Update       : 10/02/2019
# Description  : Class representing a graph abstract data type (ADT)
# Copyright    : Copyright (c) 2019 by Anthony Rey
# License      : Creative Common Attribution-ShareAlike 4.0 International
#========================================

#========================================
# Links
#========================================

# 

#========================================
# Packages/modules
#========================================

# Python core packages/modules

# Python extension packages/modules

#========================================
# Classes
#========================================

# Class representing a graph ADT 
class Graph:
    """
    """

    # 
    def __init__(self, graph_dictionary):
        self.graph = graph_dictionary

    # Return the edges of the graph 
    def get_edges(self):
        """
        """
        # Define a list of edges 
        edges = []
        # Iterate through all the nodes of the graph 
        for node in self.graph:
            # For each node, iterate through all its neighbors
            for neighbor in self.graph[node]:
                # Append to the list of edges, a tuple (node, neighbor) representing an edge
                edges.append((node, neighbor))
        # Return the list of edges 
        return edges 

    # Return the isolated nodes of the graph 
    def get_isolated_nodes(self):
        """

        """
        # Define a list for isolated nodes 
        isolated_nodes = []
        # Iterate through all the nodes of the graph
        for node in self.graph:
            # If a node is empty (no neighbors), then it is isolated
            if not self.graph[node]:
                # Add the isolated node to the list of isolated nodes
                isolated_nodes += node 
        # Return the list of isolated nodes
        return isolated_nodes

#========================================
# Functions 
#========================================

