import json
import yaml
import os


def data_load(file_path: str):
    with open(file_path, 'r') as file:
        data = file.read()
        extension = os.path.splitext(file_path)[1]
    return parse_data(data, extension)


def parse_data(data, extension):
    if extension in (".yml", ".yaml"):
        return yaml.safe_load(data)
    elif extension == ".json":
        return json.loads(data)
    else:
        raise ValueError(f"Unsupported file format: {extension}")
