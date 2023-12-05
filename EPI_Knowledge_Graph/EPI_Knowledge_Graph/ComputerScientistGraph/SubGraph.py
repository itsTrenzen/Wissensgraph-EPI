from platform import node


class SubGraph:

    def __init__(self, Node: node, sources, connections):
        self.node = node
        self.sources = sources
        self.connections = connections

    def connect(self, nodes):
        self.node.connect()
        
