from itertools import repeat

from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.Nodes_Init import *


def sub_graph(parent_node: Node, nodes):
    list(map(connect_to_node, repeat(parent_node), nodes))


def connect_to_node(parent_node: Node, node: Node):
    parent_node.connect(node)


class Graph:

    def __init__(self):
        sub_graph(TIM_BERNERS_LEE, [])
