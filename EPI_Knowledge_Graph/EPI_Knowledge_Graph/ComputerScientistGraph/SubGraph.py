from itertools import repeat
from platform import node

from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.IdNode import IdNode


class SubGraph:

    def __init__(self, root_node, sources, connections):
        self.node = root_node
        self.src = sources
        self.conn = connections

    def connect(self, nodes):
        list(map(self.connect_to_node, nodes))

    def __connect_to_node(self, conn_node: IdNode):
        if self.node.id == conn_node:
            self.connect(node)
