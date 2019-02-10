#=========================================
# coding = utf-8
#=========================================
# Name         : test_graph.py 
# Author       : Anthony Rey
# Version      : 1.0.0.0
# Date         : 10/02/2019
# Update       : 10/02/2019
# Description  : Test the Graph class's methods
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
try:
    import unittest
except ImportError:
    raise ImportError("Sorry, but the \"unittest\" module/package is required to run this program!")

# Python extension packages/modules
from ..production import graph

#========================================
# Classes
#========================================

# Test the Graph class's methods 
class TestGraph(unittest.TestCase):
    """
    """

    #
    def setUp(self):
        """
        """
        #
        self.graph_dictionary = {'a': ['b','d'],
                                 'b': ['a','c','d','e'],
                                 'c': ['b'],
                                 'd': ['a','b'],
                                 'e': ['b','f'],
                                 'f': ['e'],
                                 'g': []}
        # 
        self.graph = graph.Graph(self.graph_dictionary)

    def test_graph_edges_search(self):
        # Check that the edges are the ones given
        self.assertEqual(len(self.graph.get_edges()), 12)

    def test_graph_isolated_nodes_search(self):
        # Check that the isolated nodes are the ones given
        self.assertEqual(self.graph.get_isolated_nodes(), ['g'])


    def tearDown(self):
        pass




# --------------------------------------------------------------------

# FUNCTIONS 

# --------------------------------------------------------------------



#:::: Execute (main function) ::::#

if __name__ == '__main__':

        unittest.main() 


