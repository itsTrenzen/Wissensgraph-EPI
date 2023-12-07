from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel.Node import Node


class ExtendedNode(Node):

    def __init__(self, description, titel, connections, image_name="image_placeholder.png", x=0, y=0):
        super.__init__(description, titel, image_name, x=0, y=0)
        self.__connect(connections)

    def __connect(self, connections):
        for conn in connections:
            self.connect(conn)
