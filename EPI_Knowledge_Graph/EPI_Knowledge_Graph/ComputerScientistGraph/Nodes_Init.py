# Node constants
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.KnowledgeNodes.Awards import \
    Turing_Award_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.KnowledgeNodes.Computer import ENIAC_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.KnowledgeNodes.Organizations import \
    World_Wide_Web_Consortium_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.KnowledgeNodes.WebTechnologies import \
    World_Wide_Web_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel import Graph
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel.Node import Node
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.KnowledgeNodes.ComputerScientists import \
    Tim_Berners_Lee_Data, John_William_Mauchly_Data, Alan_Turing_Data, Alonzo_Church_Data


class Nodes:
    def __init__(self, graph: Graph):
        graph.add_new_node_to_graph(TIM_BERNERS_LEE)
        graph.add_new_node_to_graph(ALAN_TURING)
        graph.add_new_node_to_graph(ALONZO_CHURCH)
        graph.add_new_node_to_graph(JOHN_WILLIAM_MAUCHLY)
        graph.add_new_node_to_graph(WORLD_WIDE_WEB_CONSORTIUM)
        graph.add_new_node_to_graph(TURING_AWARD_DATA)
        graph.add_new_node_to_graph(ENIAC)


TIM_BERNERS_LEE = Node(
    Tim_Berners_Lee_Data.CONTENT,
    Tim_Berners_Lee_Data.TITEL,
    Tim_Berners_Lee_Data.IMAGE_NAME)

ALAN_TURING = Node(
    Alan_Turing_Data.CONTENT,
    Alan_Turing_Data.TITEL,
    Alan_Turing_Data.IMAGE_NAME)

ALONZO_CHURCH = Node(
    Alonzo_Church_Data.CONTENT,
    Alonzo_Church_Data.TITEL,
    Alonzo_Church_Data.IMAGE_NAME)

JOHN_WILLIAM_MAUCHLY = Node(
    John_William_Mauchly_Data.CONTENT,
    John_William_Mauchly_Data.TITEL,
    John_William_Mauchly_Data.IMAGE_NAME)

WORLD_WIDE_WEB_CONSORTIUM = Node(
    World_Wide_Web_Consortium_Data.CONTENT,
    World_Wide_Web_Consortium_Data.TITEL,
    World_Wide_Web_Consortium_Data.IMAGE_NAME)

TURING_AWARD_DATA = Node(
    Turing_Award_Data.CONTENT,
    Turing_Award_Data.TITEL,
    Turing_Award_Data.IMAGE_NAME)

ENIAC = Node(
    ENIAC_Data.CONTENT,
    ENIAC_Data.TITEL,
    ENIAC_Data.IMAGE_NAME)
