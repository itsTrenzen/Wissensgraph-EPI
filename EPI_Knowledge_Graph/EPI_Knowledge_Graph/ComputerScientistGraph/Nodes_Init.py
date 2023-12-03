# Node constants
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel import Graph
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel.Node import Node
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.ComputerScientists import \
    TimBernersLee_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.ComputerScientists import \
    AlanTuring_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.ComputerScientists import \
    AlonzoChurch_Data


class Nodes:
    def __init__(self, graph: Graph):
        graph.add_new_node_to_graph(TIM_BERNERS_LEE)
        graph.add_new_node_to_graph(ALAN_TURING)
        graph.add_new_node_to_graph(ALONZO_CHURCH)


TIM_BERNERS_LEE = Node(TimBernersLee_Data.CONTENT, TimBernersLee_Data.TITEL, TimBernersLee_Data.IMAGE_NAME)
ALAN_TURING = Node(AlanTuring_Data.CONTENT, AlanTuring_Data.TITEL, AlanTuring_Data.IMAGE_NAME)
ALONZO_CHURCH = Node(AlonzoChurch_Data.CONTENT, AlonzoChurch_Data.TITEL, AlonzoChurch_Data.IMAGE_NAME)
