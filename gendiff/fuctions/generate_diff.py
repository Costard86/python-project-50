import json
import yaml


def generate_diff(file1, file2):
    data1 = data_load(file1)
    data2 = data_load(file2)

    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    all_keys = sorted(keys1.union(keys2))

    lines = ['{\n']
    for key in all_keys:
        value1 = true_false_lower(data1.get(key))
        value2 = true_false_lower(data2.get(key))

        if key not in keys2:
            lines.append(f" - {key}: {value1}\n")
        elif key not in keys1:
            lines.append(f" + {key}: {value2}\n")
        elif value1 != value2:
            lines.append(f" - {key}: {value1}\n")
            lines.append(f" + {key}: {value2}\n")
        else:
            lines.append(f"   {key}: {value1}\n")
    lines.append('}')
    return "".join(lines)


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
