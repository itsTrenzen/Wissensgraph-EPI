import os.path
import warnings
from pathlib import Path
from EPI_Knowledge_Graph.EPI_Knowledge_Graph.GraphModel.Node import Node


class ExtendedNode(Node):
    def __init__(self, description, titel, connections, image_name="image_placeholder.png", x=0, y=0):
        super().__init__(description, titel, self._process_image_name(image_name), x=x, y=y)
        self.connections = connections

    def _process_image_name(self, image_name):
        if not image_name or image_name.isspace():
            image_name = "image_placeholder.png"
            self._issue_warning("Image name is None or empty. Using default image placeholder.")
        else:
            file_path = Path(__file__).resolve().parent.parent / 'Resources' / 'Images' / image_name
            if not file_path.is_file():
                image_name = "image_placeholder.png"
                self._issue_warning(f"Image file not found: {file_path}. Using default image placeholder.")
        return image_name

    @staticmethod
    def _issue_warning(message):
        warnings.warn(message, category=UserWarning)
