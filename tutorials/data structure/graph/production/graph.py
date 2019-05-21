#=========================================
# coding = utf-8
#=========================================
# Name         : graph.py 
# Author       : Anthony Rey
# Version      : 1.0.0.0
# Date         : 10/02/2019
# Update       : 21/05/2019
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

    get_edges:

    get_isolated_nodes:

    """

    # 
    def __init__(self, graph_dictionary):
        self.graph = graph_dictionary

    # Get the edges of the graph 
    def get_edges(self):
        """
        Get the edges of the graph
        -------------------------------------------------------------
        Parameters
        ----------
        None
        
        Returns
        -------
        edges: list
            Edges of the graph (node, neighbor)
        
        Example
        -------
        >>> [('a', 'b'), ('a', 'd')] = get_edges()
        """
        # Iterate through all the nodes of the graph and all their neighbors to get the edges
        edges = [(node, neighbor) for node in self.graph for neighbor in self.graph[node]]
        # Return the list of edges
        return edges 
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
        """

    # Get the isolated nodes of the graph 
    def get_isolated_nodes(self):
        """
        Get the isolated nodes of the graph
        -------------------------------------------------------------
        Parameters
        ----------
        None
        
        Returns
        -------
        isolated_nodes: list
            Isolated nodes of the graph (name of the node with no neighbors)
        
        Example
        -------
        >>> ['g', 'i'] = get_isolated_nodes()
        """
        # Iterate through all the nodes of the graph, and store its name if isolated (no neighbors) 
        isolated_nodes = [node for node in self.graph if not self.graph[node]]
        # Return the list of isolated nodes
        return isolated_nodes 
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
        """

#========================================
# Functions 
#========================================

