import os.path
import warnings
from pathlib import Path

from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel.Node import Node


class ExtendedNode(Node):
    connections = []

    def __init__(self, description, titel, connections, image_name="image_placeholder.png", x=0, y=0):
        script_directory = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_directory, '..', 'Resources', 'Images', image_name)

        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            warnings.warn(
                message=f"Image \"{file_path}\" für Node \"{titel}\" konnte nicht gefunden werden.",
                category=UserWarning)
            image_name = "image_placeholder.png"

        super().__init__(description, titel, image_name, x=0, y=0)
        self.connections = connections
