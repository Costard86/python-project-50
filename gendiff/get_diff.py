def get_diff(data1, data2, key=None):
    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    all_keys = sorted(keys1.union(keys2))

    result = []

    for subkey in all_keys:
        value1 = data1.get(subkey)
        value2 = data2.get(subkey)

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


def to_string(data):
    if data is True:
        data = "true"
    if data is False:
        data = "false"
    if data is None:
        data = "null"
    return data
