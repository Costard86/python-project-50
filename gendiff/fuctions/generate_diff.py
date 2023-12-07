import json
import yaml
from gendiff.scripts.formating import formatting


def generate_diff(file1, file2, display_format="stylish"):
    data1 = data_load(file1)
    data2 = data_load(file2)

    diff = {'type': 'root', 'children': get_diff(data1, data2)}
    return formatting(diff, display_format)


def get_diff(data1, data2, key=None):
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    all_keys = sorted(keys1.union(keys2))

    result = []

    for subkey in all_keys:
        value1 = true_false_lower(data1.get(subkey))
        value2 = true_false_lower(data2.get(subkey))

        if (subkey in keys1 and subkey in keys2 and isinstance(value1, dict)
                and isinstance(value2, dict)):
            result.append({'type': 'dict', 'key': subkey,
                           'children': get_diff(value1, value2, key=subkey)})
        elif subkey not in keys2:
            result.append({'type': 'remove', 'key': subkey, 'value': value1})
        elif subkey not in keys1:
            result.append({'type': 'added', 'key': subkey, 'value': value2})
        elif value1 == value2:
            result.append({'type': 'same', 'key': subkey, "value": value1})
        else:
            result.append({"type": "changed", "key": subkey,
                           "value": (value1, value2)})

    return result


def true_false_lower(data):
    if data is True:
        data = 'true'
    if data is False:
        data = 'false'
    if data is None:
        data = 'null'
    return data


def data_load(file_path):
    if str(file_path).endswith(('.json', '.yaml', '.yml')):
        if str(file_path).endswith(('.yaml', '.yml')):
            return yaml.safe_load(open(file_path).read())
        else:
            return json.loads(open(file_path).read())
    else:
        raise ValueError(f"Unsupported file format: {file_path}")


def get_value(obj):
    return obj.get("value", None)
