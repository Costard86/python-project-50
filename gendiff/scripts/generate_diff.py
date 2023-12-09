import json
import yaml
from gendiff.scripts.formating import formatting
from gendiff.fuctions.get_diff import get_diff


def generate_diff(file1, file2, display_format="stylish"):
    data1 = data_load(file1)
    data2 = data_load(file2)

    diff = {'type': 'root', 'children': get_diff(data1, data2)}
    return formatting(diff, display_format)


def data_load(file_path):
    if str(file_path).endswith(('.json', '.yaml', '.yml')):
        if str(file_path).endswith(('.yaml', '.yml')):
            return yaml.safe_load(open(file_path).read())
        else:
            return json.loads(open(file_path).read())
    else:
        raise ValueError(f"Unsupported file format: {file_path}")
