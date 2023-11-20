import itertools


def format_stylish(diff, depth=0):
    lines = []
    current_indent = ' ' * depth
    for item in diff:
        key = item['key']
        value = item['value']
        item_type = item['type']

        if item_type == 'added':
            prefix = '+'
        elif item_type == 'remove':
            prefix = '-'
        else:
            prefix = ' '

        if isinstance(value, list):
            formatted_value = format_stylish(value, depth + 4)
            lines.append(f"{current_indent}{prefix} {key}: {formatted_value}")
        elif isinstance(value, dict):
            formatted_value = stringify(value, depth)
            lines.append(f"{current_indent}{prefix} {key}: {formatted_value}")
        else:
            lines.append(f"{current_indent}{prefix} {key}: {value}")

    return '{\n' + '\n'.join(lines) + '\n' + current_indent + '}'


def stringify(value, depth=0):
    if not isinstance(value, dict):
        return str(value)

    deep_indent_size = depth + 4
    deep_indent = ' ' * deep_indent_size
    current_indent = ' ' * depth
    lines = []
    for key, val in value.items():
        lines.append(f'{deep_indent}{key}: {stringify(val, deep_indent_size)}')
    result = itertools.chain(["{"], lines, [current_indent + "}"])
    return '\n'.join(result)

