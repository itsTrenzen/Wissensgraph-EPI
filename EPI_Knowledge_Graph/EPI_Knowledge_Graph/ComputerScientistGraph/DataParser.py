import os
import warnings

#from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph import JsonParser
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.ExtendedNode import ExtendedNode


def load_py_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as py_file:
        py_code = py_file.read()

    local_vars = {}
    exec(py_code, {}, local_vars)

    return local_vars


def convert_py_to_node(py_data):
    return ExtendedNode(
        py_data.get("CONTENT", ""),
        py_data.get("TITEL", ""),
        py_data.get("CONNECTIONS", []),
        py_data.get("IMAGE_NAME"))


def parse_nodes(graph, root_path):
    nodes = {}

    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file.endswith("_Data.py"):
                py_filepath = os.path.join(root, file)
                data = load_py_file(py_filepath)

                node = convert_py_to_node(data)

                node_id = file.replace("_Data.py", "").upper()
                nodes.update({node_id: node})

                graph.add_new_node_to_graph(node)

    connect_nodes(nodes)


def connect_nodes(nodes):
    for node in nodes.values():
        for conn_name in node.connections:
            conn_node = nodes.get(conn_name)

            if conn_node is None:
                warnings.warn(
                    message=f"Connection \"{conn_name}\" für Node \"{node.titel}\" nicht gefunden!",
                    category=UserWarning)
                continue

            node.connect(conn_node)
