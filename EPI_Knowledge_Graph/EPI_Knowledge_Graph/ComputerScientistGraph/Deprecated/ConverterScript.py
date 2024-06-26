import os
import json

from EPI_Knowledge_Graph.EPI_Knowledge_Graph.ComputerScientistGraph.Deprecated import JsonParser

JSON_SCHEMA = JsonParser.JSON_SCHEMA


def convert_py_to_json(py_filepath):
    with open(py_filepath, 'r', encoding='utf-8') as py_file:
        py_code = py_file.read()

    local_vars = {}
    exec(py_code, {}, local_vars)

    json_filename = os.path.splitext(py_filepath)[0] + ".json"

    json_data = {
        "id": os.path.splitext(os.path.basename(py_filepath))[0].replace("_Data", "").upper(),
        "title": local_vars.get("TITEL", ""),
        "content": local_vars.get("CONTENT", ""),
        "image": local_vars.get("IMAGE_NAME"),
        "connections": local_vars.get("CONNECTIONS", [])
    }

    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=2)

    print(f"Datei umgewandelt: {json_filename}")


def convert_folder_to_json(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith("_Data.py"):
                py_filepath = os.path.join(root, file)
                convert_py_to_json(py_filepath)


def main():
    folder_path = "../NodeData"
    convert_folder_to_json(folder_path)


if __name__ == "__main__":
    main()
