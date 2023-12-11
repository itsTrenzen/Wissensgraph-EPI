# Node constants
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.Awards import Turing_Award_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.Machines import Bombes_Data, Analytic_Engine_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.Machines.Computer import ENIAC_Data, \
    UNIVAC_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.Organizations import \
    World_Wide_Web_Consortium_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.TheoreticalInformatics import \
    Turing_Machine_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.WebTechnologies import \
    HTML_Data, WorldWideWeb_Browser_Data, World_Wide_Web_Data, Wissensbeitrag_Ada_Lovelace_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel.Graph import Graph
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel.Node import Node
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.ComputerScientists import \
    Tim_Berners_Lee_Data, John_William_Mauchly_Data, Alan_Turing_Data, Alonzo_Church_Data, John_Presper_Eckert_Data, Ada_Lovelace_Data, \
    Charles_Babbage_Data, Grace_Hopper_Data

class Nodes:
    def __init__(self, graph: Graph):
        graph.add_new_node_to_graph(TIM_BERNERS_LEE)
        graph.add_new_node_to_graph(ALAN_TURING)
        graph.add_new_node_to_graph(ALONZO_CHURCH)
        graph.add_new_node_to_graph(JOHN_WILLIAM_MAUCHLY)
        graph.add_new_node_to_graph(JON_PRESPER_ECKERT)
        graph.add_new_node_to_graph(WORLD_WIDE_WEB_CONSORTIUM)
        graph.add_new_node_to_graph(TURING_AWARD)
        graph.add_new_node_to_graph(ENIAC)
        graph.add_new_node_to_graph(UNIVAC)
        graph.add_new_node_to_graph(HTML)
        graph.add_new_node_to_graph(WORLD_WIDE_WEB_BROWSER)
        graph.add_new_node_to_graph(WORLD_WIDE_WEB)
        graph.add_new_node_to_graph(BOMBES)
        graph.add_new_node_to_graph(TURING_MACHINE)
        graph.add_new_node_to_graph(ADA_LOVELACE)
        graph.add_new_node_to_graph(CHARLES_BABBAGE)
        graph.add_new_node_to_graph(ANALYTIC_ENGINE)
        graph.add_new_node_to_graph(WISSENSBEITRAG_ADA_LOVELACE)
        graph.add_new_node_to_graph(GRACE_HOPPER)


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

JON_PRESPER_ECKERT = Node(
    John_Presper_Eckert_Data.CONTENT,
    John_Presper_Eckert_Data.TITEL,
    John_Presper_Eckert_Data.IMAGE_NAME)

WORLD_WIDE_WEB_CONSORTIUM = Node(
    World_Wide_Web_Consortium_Data.CONTENT,
    World_Wide_Web_Consortium_Data.TITEL,
    World_Wide_Web_Consortium_Data.IMAGE_NAME)

TURING_AWARD = Node(
    Turing_Award_Data.CONTENT,
    Turing_Award_Data.TITEL,
    Turing_Award_Data.IMAGE_NAME)

ENIAC = Node(
    ENIAC_Data.CONTENT,
    ENIAC_Data.TITEL,
    ENIAC_Data.IMAGE_NAME)

UNIVAC = Node(
    UNIVAC_Data.CONTENT,
    UNIVAC_Data.TITEL,
    UNIVAC_Data.IMAGE_NAME)

HTML = Node(
    HTML_Data.CONTENT,
    HTML_Data.TITEL,
    HTML_Data.IMAGE_NAME)

WORLD_WIDE_WEB_BROWSER = Node(
    WorldWideWeb_Browser_Data.CONTENT,
    WorldWideWeb_Browser_Data.TITEL,
    WorldWideWeb_Browser_Data.IMAGE_NAME)

WORLD_WIDE_WEB = Node(
    World_Wide_Web_Data.CONTENT,
    World_Wide_Web_Data.TITEL,
    World_Wide_Web_Data.IMAGE_NAME)

BOMBES = Node(
    Bombes_Data.CONTENT,
    Bombes_Data.TITEL,
    Bombes_Data.IMAGE_NAME)

TURING_MACHINE = Node(
    Turing_Machine_Data.CONTENT,
    Turing_Machine_Data.TITEL,
    Turing_Machine_Data.IMAGE_NAME)

#Jaschas Nodes
ADA_LOVELACE = Node(
    Ada_Lovelace_Data.CONTENT,
    Ada_Lovelace_Data.TITEL,
    Ada_Lovelace_Data.IMAGE_NAME
)
CHARLES_BABBAGE = Node(
    Charles_Babbage_Data.CONTENT,
    Charles_Babbage_Data.TITEL,
    Charles_Babbage_Data.IMAGE_NAME
)
ANALYTIC_ENGINE = Node(
    Analytic_Engine_Data.CONTENT,
    Analytic_Engine_Data.TITEL,
    Analytic_Engine_Data.IMAGE_NAME
)
WISSENSBEITRAG_ADA_LOVELACE = Node(
    Wissensbeitrag_Ada_Lovelace_Data.CONTENT,
    Wissensbeitrag_Ada_Lovelace_Data.TITEL
)
GRACE_HOPPER = Node(
    Grace_Hopper_Data.CONTENT,
    Grace_Hopper_Data.TITEL,
    Grace_Hopper_Data.IMAGE_NAME
)