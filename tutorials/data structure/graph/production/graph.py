#=========================================
# coding = utf-8
#=========================================
# Name         : graph.py 
# Author       : Anthony Rey
# Version      : 1.0.0.0
# Date         : 10/02/2019
# Update       : 26/05/2019
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
    Methods
    ------- 
    add_nodes(nodes):
        Add nodes to the graph
    add_edges(edges):
        Add edges to the graph
    get_nodes():
        Get the nodes of the graph
    get_edges(): 
        Get the edges of the graph 
    get_isolated_nodes(): 
        Get the isolated nodes of the graph
    find_shortest_path(starting_node, ending_node):
        Find the shortest path between two nodes
    find_paths(starting_node, ending_node)
        Find all possible paths between two nodes
    """

    # Constructor/initializer of the Graph class 
    def __init__(self, graph_dictionary):
        """
        Initialize/construct an object of the Graph class
        -------------------------------------------------------------
        Parameters
        ----------
        graph_dictionary: dict
            Dictionary representing the graph
        
        Returns
        -------
        None
        
        Example
        -------
        >>> graph = Graph({'a':[]})
        """
        # Store the dictionary in the hidden variable _graph
        self._graph = graph_dictionary

    # Add nodes to the graph
    def add_nodes(self, nodes):
        """
        Add nodes to the graph
        -------------------------------------------------------------
        Parameters
        ----------
        nodes: list
            List of nodes to be added to the graph
        
        Returns
        -------
        None
        
        Example
        -------
        >>> {'a': ['b'], 'a': ['b'], 'g': [], 'f': []} = add_node(['g', 'f'])
        """
        # Add all nodes (without neighbor) which do not belong to the graph yet
        self._graph.update({node: [] for node in nodes if node not in self._graph})

    # Add edges to the graph
    def add_edges(self, edges):
        """
        Add edges of the graph
        -------------------------------------------------------------
        Parameters
        ----------
        edges: list
            Edges of the graph (node, neighbor)
        
        Returns
        -------
        None
        
        Example
        -------
        >>> [('a', 'b'), ('a', 'd')] = get_edges()
        """
        #
        for (node_one, node_two) in edges:
            if node_one in self._graph: 
                self._graph[node_one].append(node_two)
            else:
                self._graph[node_one] = node_two 
            if node_two in self._graph: 
                self._graph[node_two].append(node_one)
            else:
                self._graph[node_two] = node_one 
            
        # TO DO 
        # [self._graph[node_one].append(node_two) for (node_one, node_two) in edges if node_one in self._graph]
 
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
        edges = [(node, neighbor) for node in self._graph for neighbor in self._graph[node]]
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
        isolated_nodes = [node for node in self._graph if not self._graph[node]]
        # Return the list of isolated nodes
        return isolated_nodes 
        """
        # Define a list for isolated nodes 
        isolated_nodes = []
        # Iterate through all the nodes of the graph
        for node in self.graph:
            # If a node is empty (no neighbors), then it is isolated
            if not self._graph[node]:
                # Add the isolated node to the list of isolated nodes
                isolated_nodes += node 
        # Return the list of isolated nodes
        return isolated_nodes
        """
    
    def __str__(self):
        description  = "Nodes: " + "".join(str(node) + " " for node in self._graph)
        description += "\nEdges: " + "".join(str(edge) in self.get_edges()) 
        return description

#========================================
# Functions 
#========================================

