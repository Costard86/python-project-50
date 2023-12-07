def format_plane(diff, path=""):

    result = ""

    for item in diff['children']:
        item_type = item['type']
        key = item['key']
        item_path = f"{path}.{key}" if path else key

        if item_type == 'dict':
            result += format_plane(item, path=item_path)
        else:
            if item_type == 'added':
                result += (f"Property '{item_path}' was added with "
                           f"value: {format_value(item['value'])}\n")
            elif item_type == 'remove':
                result += f"Property '{item_path}' was removed\n"
            elif item_type == 'changed':
                old_value, new_value = item['value']
                result += (f"Property '{item_path}' was updated. "
                           f"From {format_value(old_value)} to "
                           f"{format_value(new_value)}\n")

    return result


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str) and value in ('true', 'false', 'null'):
        return value
    elif isinstance(value, str):
        return f"'{value}'"
    return value
