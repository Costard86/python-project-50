from pathlib import Path
from gendiff.fuctions.generate_diff import generate_diff


def get_path(file_name):
    p = Path(__file__)
    tests = p.absolute().parent
    return tests/'fixtures'/file_name


def test_merge(tmp_path):
    file1 = get_path('file1.json')
    file2 = get_path('file2.json')
    expected = ('{\n - follow: False\n   host: hexlet.io\n '
                '- proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n '
                '+ verbose: True\n}')

    result = generate_diff(file1, file2)
    assert result == expected


def test_merge_same_text(tmp_path):
    file1 = get_path('file1.json')
    file2 = get_path('file3.json')
    expected = ('{\n   follow: False\n   host: hexlet.io\n   '
                'proxy: 123.234.53.22\n   timeout: 50\n}')

    result = generate_diff(file1, file2)
    assert result == expected
