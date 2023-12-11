import glob
import warnings

import jsonref
from jsonschema import validate

from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.ExtendedNode import ExtendedNode

JSON_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "title": {"type": "string"},
        "content": {"type": "string"},
        "image": {"type": "string"},
        "connections": {
            "type": "array",
            "items": {"$ref": "#/properties/id"}
        }
    },
    "required": ["id", "title", "content", "image", "connections"]
}


class JsonParser:

    def __init__(self, graph, root_dir):
        self.root = graph
        self.file_paths = glob.glob(root_dir + '/**/*.json', recursive=True)
        self.nodes = {}

    def parse_nodes(self):
        all_data = {}

        for file_path in self.file_paths:
            data = JsonParser.__load_json_file(file_path)
            all_data[file_path] = jsonref.replace_refs(data)

        for file_path, resolved_data in all_data.items():
            try:
                validate(instance=resolved_data, schema=JSON_SCHEMA)
                print(f"Validierung erfolgreich für {file_path}")
            except Exception as e:
                print(f"Fehler bei der Validierung für {file_path}: {e}")
                return
            node = ExtendedNode(
                resolved_data["content"],
                resolved_data["title"],
                resolved_data["connections"],
                resolved_data["image"])

            self.nodes.update({resolved_data["id"]: node})
            self.root.add_new_node_to_graph(node)

    def connect_nodes(self):
        for node in self.nodes.values():

            for conn_name in node.connections:
                conn_node = self.nodes.get(conn_name)

                if conn_node is None:
                    warnings.warn(
                        message=f"Connection \"{conn_name}\" für Node \"{node.titel}\" nicht gefunden!",
                        category=UserWarning)
                    return

                node.connect(conn_node)

    @staticmethod
    def __load_json_file(file_path):
        with open(file_path, 'r') as file:
            return jsonref.load(file)
