import glob
import json
from jsonschema import validate

from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.IdNode import IdNode
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.SubGraph import SubGraph
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel import Node

JSON_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "TYPE": {"type": "string"},
        "ID": {"type": "string"},
        "TITLE": {"type": "string"},
        "CONTENT": {"type": "string"},
        "SOURCES": {
            "type": "array",
            "items": {"type": "string"}
        },
        "CONNECTIONS": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": ["TYPE", "ID", "TITLE", "CONTENT", "SOURCES", "CONNECTIONS"]
}


def parse_json(root_dir, recursive):
    nodes = list
    subgraphs = list

    for filename in glob.iglob(root_dir + '**/*.json', recursive=recursive):
        json_content = json.load(filename)
        validate(instance=json_content, schema=JSON_SCHEMA)

        node = IdNode(json_content["ID"],
                      json_content["CONTENT"],
                      json_content["TITLE"],
                      json_content["IMAGE"])

        nodes.append(node)
        subgraphs.append(SubGraph(node, json_content["SOURCES"], json_content["CONNECTIONS"]))

    for s in subgraphs:
        s.connect(nodes)
