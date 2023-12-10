# Node constants
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.Awards import Turing_Award_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.Machines import Bombes_Data, \
    Unix_Data, Programmierbare_ICs_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.Machines.Computer import ENIAC_Data, \
    UNIVAC_Data, Lilith_Data, Ceres_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.ProgrammingLanguages import Sprache_B_Data, \
    Sprache_C_Data, Sprache_Pascal_Data, Sprache_Algol_Data, Sprache_Modula2_Data, Sprache_Euler_Data, Sprache_Oberon_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.Organizations import \
    World_Wide_Web_Consortium_Data, Bell_Labs_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.WebTechnologies import \
    HTML_Data, WorldWideWeb_Browser_Data, World_Wide_Web_Data, Arpanet_Data
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel.Graph import Graph
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel.Node import Node
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.NodeData.ComputerScientists import \
    Tim_Berners_Lee_Data, John_William_Mauchly_Data, Alan_Turing_Data, Alonzo_Church_Data, John_Presper_Eckert_Data, \
    Robert_Cailliau_Data, Kenneth_Lane_Thompson_Data, Ray_Tomlinson_Data, Dennis_Ritchie_Data, Niklaus_Wirth_Data


class Nodes:
    def __init__(self, graph: Graph):
        graph.add_new_node_to_graph(BEKANNTESTE_INF)
        graph.add_new_node_to_graph(TIM_BERNERS_LEE)
        graph.add_new_node_to_graph(ALAN_TURING)
        graph.add_new_node_to_graph(ALONZO_CHURCH)
        graph.add_new_node_to_graph(JOHN_WILLIAM_MAUCHLY)
        graph.add_new_node_to_graph(JON_PRESPER_ECKERT)
        graph.add_new_node_to_graph(WORLD_WIDE_WEB_CONSORTIUM)
        graph.add_new_node_to_graph(TURING_AWARD_DATA)
        graph.add_new_node_to_graph(ENIAC)
        graph.add_new_node_to_graph(UNIVAC)
        graph.add_new_node_to_graph(HTML)
        graph.add_new_node_to_graph(WORLD_WIDE_WEB_BROWSER)
        graph.add_new_node_to_graph(WORLD_WIDE_WEB)
        graph.add_new_node_to_graph(BOMBES)
        graph.add_new_node_to_graph(ROBERT_CAILLIAU)
        graph.add_new_node_to_graph(KENNETH_LANE_THOMPSON)
        graph.add_new_node_to_graph(RAY_TOMLINSON)
        graph.add_new_node_to_graph(DENNIS_RITCHIE)
        graph.add_new_node_to_graph(NIKLAUS_WIRTH)
        graph.add_new_node_to_graph(UNIX)
        graph.add_new_node_to_graph(ARPANET)
        graph.add_new_node_to_graph(BELL_LABS)
        graph.add_new_node_to_graph(SPRACHE_B)
        graph.add_new_node_to_graph(SPRACHE_C)
        graph.add_new_node_to_graph(SPRACHE_PASCAL)
        graph.add_new_node_to_graph(SPRACHE_ALGOL)
        graph.add_new_node_to_graph(LILITH)
        graph.add_new_node_to_graph(CERES)
        graph.add_new_node_to_graph(SPRACHE_MODULA2)
        graph.add_new_node_to_graph(SPRACHE_EULER)
        graph.add_new_node_to_graph(SPRACHE_OBERON)
        graph.add_new_node_to_graph(ICS)

BEKANNTESTE_INF = Node("","Bekannteste Informatiker\nund ihre Beiträge")

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

TURING_AWARD_DATA = Node(
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
#Nicks Nodes
ROBERT_CAILLIAU = Node(
    Robert_Cailliau_Data.CONTENT,
    Robert_Cailliau_Data.TITEL#,
    #Robert_Cailliau_Data.IMAGE_NAME
)
KENNETH_LANE_THOMPSON = Node(
    Kenneth_Lane_Thompson_Data.CONTENT,
    Kenneth_Lane_Thompson_Data.TITEL#,
    #Kenneth_Lane_Thompson_Data.IMAGE_NAME
)
RAY_TOMLINSON = Node(
    Ray_Tomlinson_Data.CONTENT,
    Ray_Tomlinson_Data.TITEL#,
    #Kenneth_Lane_Thompson_Data.IMAGE_NAME
)
DENNIS_RITCHIE = Node(
    Dennis_Ritchie_Data.CONTENT,
    Dennis_Ritchie_Data.TITEL#,
    #Dennis_Ritchie_Data.IMAGE_NAME
)
NIKLAUS_WIRTH = Node(
    Niklaus_Wirth_Data.CONTENT,
    Niklaus_Wirth_Data.TITEL#,
    #Niklaus_Wirth_Data.IMAGE_NAME
)
UNIX = Node(
    Unix_Data.CONTENT,
    Unix_Data.TITEL#,
    #Unix_Data.IMAGE_NAME
)
ARPANET = Node(
    Arpanet_Data.CONTENT,
    Arpanet_Data.TITEL#,
    #Arpanet_Data.IMAGE_NAME
)
BELL_LABS = Node(
    Bell_Labs_Data.CONTENT,
    Bell_Labs_Data.TITEL#,
    #Bell_Labs_Data.IMAGE_NAME
)
SPRACHE_B = Node(
    Sprache_B_Data.CONTENT,
    Sprache_B_Data.TITEL#,
    #Sprache_B_Data.IMAGE_NAME
)
SPRACHE_C = Node(
    Sprache_C_Data.CONTENT,
    Sprache_C_Data.TITEL#,
    #Sprache_C_Data.IMAGE_NAME
)
SPRACHE_PASCAL = Node(
    Sprache_Pascal_Data.CONTENT,
    Sprache_Pascal_Data.TITEL#,
    #Sprache_Pascal_Data.IMAGE_NAME
)
SPRACHE_ALGOL = Node(
    Sprache_Algol_Data.CONTENT,
    Sprache_Algol_Data.TITEL#,
    #Sprache_Algol_Data.IMAGE_NAME
)
LILITH = Node(
    Lilith_Data.CONTENT,
    Lilith_Data.TITEL#,
    #Lilith_Data.IMAGE_NAME
)
CERES = Node(
    Ceres_Data.CONTENT,
    Ceres_Data.TITEL#,
    #Ceres_Data.IMAGE_NAME
)
SPRACHE_MODULA2 = Node(
    Sprache_Modula2_Data.CONTENT,
    Sprache_Modula2_Data.TITEL#,
    #Sprache_Modula2_Data.IMAGE_NAME
)
SPRACHE_EULER = Node(
    Sprache_Euler_Data.CONTENT,
    Sprache_Euler_Data.TITEL#,
    #Sprache_Euler_Data.IMAGE_NAME
)
SPRACHE_OBERON = Node(
    Sprache_Oberon_Data.CONTENT,
    Sprache_Oberon_Data.TITEL#,
    #Sprache_Oberon_Data.IMAGE_NAME
)
ICS = Node (
    Programmierbare_ICs_Data.CONTENT,
    Programmierbare_ICs_Data.TITEL#,
    #Programmierbare_ICs_Data.IMAGE_NAME
)