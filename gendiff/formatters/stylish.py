from gendiff.get_diff import to_string


def format_stylish(diff, depth=0):

    node_type = diff['type']
    children = diff.get("children")

    if node_type == "root":
        lines = map(lambda node: format_stylish(node, depth + 1), children)
        lines = "\n".join(lines).rstrip()
        return f"{{\n{lines}\n}}"

    key = diff['key']
    values = diff.get("value", None)

    if node_type == "dict":
        line = ident_deep(depth, " ") + f"{key}: "

        ends = map(lambda node: format_stylish(node, depth + 1), children)
        ends = "\n".join(ends)

        line += f"{{\n{ends}\n" + ident_deep(depth, ' ') + "}"
        return line.rstrip()

    elif node_type == "changed":
        lines = []
        for symbol, value in zip(("-", "+"), values):
            indent = ident_deep(depth, symbol)
            line = indent + f"{key}: {stringify(value, depth + 1)}"
            lines.append(line)
        return "\n".join(lines)

    elif node_type == "same":
        indent = ident_deep(depth, " ")
        return indent + f"{key}: {stringify(values, depth + 1)}"

    elif node_type == "added":
        indent_plus = ident_deep(depth, "+")
        return indent_plus + f"{key}: {stringify(values, depth + 1)}"

    elif node_type == "remove":
        indent_minus = ident_deep(depth, "-")
        return indent_minus + f"{key}: {stringify(values, depth + 1)}"

    else:
        raise ValueError("Unknown node type")


def stringify(value, depth):
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            line = f'{ident_deep(depth, " ")}{key}: {stringify(val, depth + 1)}'
            lines.append(line)

        result = "\n".join(lines)
        return f"{{\n{result}\n{ident_deep(depth - 1, ' ')}}}"

    return str(to_string(value))


def ident_deep(depth, symbol, replacer=" "):
    return f"{(depth * 4 - 2) * replacer}{symbol} "
