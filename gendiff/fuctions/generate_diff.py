import json


def generate_diff(file1, file2):
    data1 = json.loads(open(file1).read())
    data2 = json.loads(open(file2).read())

    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    all_keys = sorted(keys1.union(keys2))

    lines = ['{\n']
    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key not in keys2:
            lines.append(f"- {key} : {value1}\n")
        elif key not in keys1:
            lines.append(f"+ {key} : {value2}\n")
        elif value1 != value2:
            lines.append(f"- {key} : {value1}\n")
            lines.append(f"+ {key} : {value2}\n")
        else:
            lines.append(f"  {key} : {value1}\n")
    lines.append('}')
    return " ".join(lines)
