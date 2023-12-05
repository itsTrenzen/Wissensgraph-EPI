import glob
import json
from jsonschema import validate

from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel import Node

JSON_SCHEMA = {
  "nodeType": "string",
  "id": "string",
  "title": "string",
  "content": "string",
  "image": "string",
  "sources": [
    {"id": "ALAN_TURING_SOURCE_1" },
    {"ID": "ALAN_TURING_SOURCE_2" }
  ],
  "connections": [
    {"ID":  "TURING_AWARD"},
    {"ID":  "BOMBES"},
    {"ID":  "TURING_MACHINE"}
  ]
}

JSON_SCHEMA = {
  "type": "object",
  "properties": {
      "nodeType" : {"type": "string"},
      "id" : {"type": "string"},
      "title" : {"type": "string"},
      "content" : {"type": "string"},
      "image" : {"type": "string"},
      "sources" : {
          "type": "array",
          "properties": {
              
          }
        },
  }
}



def parse_json(root_dir, recursive):
    nodes = list
    subgraphs = list

    for filename in glob.iglob(root_dir + '**/*.json', recursive=True):
        jsonContent = json.load(filename)
        validate(instance=jsonContent, schema=JSON_SCHEMA)

        node = creNode(jsonContent)

        nodes.append(node)
        subgraphs.append(node)

def creNode(jsonContent):
    return Node(
        jsonContent["content"], 
        jsonContent["title"], 
        jsonContent["image"])

def creGraph(jsonContent, node)
    