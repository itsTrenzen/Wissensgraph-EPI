# Node constants
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel import Graph
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel.Node import Node
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.ComputerScientists import \
    TimBernersLee_Data


class Nodes:
    def __init__(self, graph: Graph):
        graph.add_new_node_to_graph(TIM_BERNERS_LEE)


TIM_BERNERS_LEE = Node(TimBernersLee_Data.CONTENT, TimBernersLee_Data.TITEL, TimBernersLee_Data.IMAGE_NAME)
