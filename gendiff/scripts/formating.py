from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plane import format_plane
from gendiff.formatters.json import format_json


FORMATES = {
    'stylish': format_stylish,
    'plane': format_plane,
    'json': format_json
}


def formatting(diff, format_="stylish"):
    try:
        func = FORMATES[format_]
    except KeyError:
        raise ValueError("ERROR: Wrong format style!")

    return func(diff)
