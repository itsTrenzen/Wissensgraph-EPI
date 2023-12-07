import glob
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
        "connections": {
            "type": "array",
            "items": {"$ref": "#/properties/id"}
        }
    },
    "required": ["id", "title", "content", "connections"]
}


class JsonParser:

    def __init__(self, graph, root_dir):
        self.root = graph
        self.file_paths = glob.iglob(root_dir + '**/*.json')
        self.validate_and_create()

    def load_json_file(self, file_path):
        with open(file_path, 'r') as file:
            return jsonref.load(file)

    def validate_and_create(self):
        all_data = {}

        for file_path in self.file_paths:
            data = self.load_json_file(file_path)
            all_data[file_path] = jsonref.replace_refs(data)

        for file_path, resolved_data in all_data.items():
            try:
                validate(instance=resolved_data, schema=JSON_SCHEMA)
                print(f"Validierung erfolgreich für {file_path}")

                node = ExtendedNode(resolved_data["content"],
                                    resolved_data["title"],
                                    resolved_data["connections"],
                                    resolved_data["image"])
                self.root.add_new_node_to_graph(node)
            except Exception as e:
                print(f"Fehler bei der Validierung für {file_path}: {e}")
