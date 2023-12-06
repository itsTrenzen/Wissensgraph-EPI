from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel.Node import Node


class IdNode(Node):

    def __init__(self, node_id, description, titel, sources, connections, image_name="image_placeholder.png", x=0, y=0):
        super.__init__(description, titel, image_name="Image_placeholder.png", x=0, y=0)
        self.id = node_id
        self.src = sources
        self.conn = connections

    def connect(self, nodes):
        list(map(self.connect_to_node, nodes))

    def __connect_to_node(self, conn_node: IdNode):
        if self.node.id == conn_node:
            self.connect(node)
