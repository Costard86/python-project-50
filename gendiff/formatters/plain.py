from gendiff.get_diff import to_string


def format_plain(diff, path=""):
    result_lines = []

    for item in diff['children']:
        item_type = item['type']
        key = item['key']
        item_path = f"{path}.{key}" if path else key

        if item_type == 'dict':
            result_lines.extend(format_plain(item, path=item_path).splitlines())
        else:
            if item_type == 'added':
                result_lines.append(f"Property '{item_path}' was added with "
                                    f"value: {format_value(item['value'])}")
            elif item_type == 'remove':
                result_lines.append(f"Property '{item_path}' was removed")
            elif item_type == 'changed':
                old_value, new_value = item['value']
                result_lines.append(
                    f"Property '{item_path}' was updated. From "
                    f"{format_value(old_value)} to {format_value(new_value)}")

    return '\n'.join(result_lines)


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif value in (False, True, None):
        return to_string(value)
    elif isinstance(value, str):
        return f"'{value}'"
    return value
