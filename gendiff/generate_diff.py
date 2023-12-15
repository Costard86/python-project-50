from gendiff.formating import formatting
from gendiff.get_diff import get_diff
from gendiff.scripts.parse_data import data_load


def generate_diff(file1, file2, display_format="stylish"):
    data1 = data_load(file1)
    data2 = data_load(file2)

    diff = {'type': 'root', 'children': get_diff(data1, data2)}
    return formatting(diff, display_format)
