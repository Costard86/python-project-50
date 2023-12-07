from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plane import format_plane


FORMATES = {
    'stylish': format_stylish,
    'plane': format_plane
}


def formatting(diff, format_="stylish"):
    try:
        func = FORMATES[format_]
    except KeyError:
        raise ValueError("ERROR: Wrong format style!")

    return func(diff)
