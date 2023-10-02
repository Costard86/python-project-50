from pathlib import Path
from gendiff.fuctions.generate_diff import generate_diff
from gendiff.fuctions.generate_diff import data_load


def get_path(file_name):
    p = Path(__file__)
    tests = p.absolute().parent
    return tests/'fixtures'/file_name


def test_merge(tmp_path):
    file1 = get_path('file1.json')
    file2 = get_path('file2.json')
    expected = ('{\n - follow: false\n   host: hexlet.io\n '
                '- proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n '
                '+ verbose: true\n}')

    result = generate_diff(file1, file2)
    assert result == expected


def test_merge_yml_json(tmp_path):
    file1 = get_path('filepath1.yml')
    file2 = get_path('file2.json')
    expected = ('{\n - follow: false\n   host: hexlet.io\n '
                '- proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n '
                '+ verbose: true\n}')

    result = generate_diff(file1, file2)
    assert result == expected


def test_merge_same_text(tmp_path):
    file1 = get_path('file1.json')
    file2 = get_path('file3.json')
    expected = ('{\n   follow: false\n   host: hexlet.io\n   '
                'proxy: 123.234.53.22\n   timeout: 50\n}')

    result = generate_diff(file1, file2)
    assert result == expected


def test_merge_same_text_yml_json(tmp_path):
    file1 = get_path('filepath1.yml')
    file2 = get_path('file1.json')
    expected = ('{\n   follow: false\n   host: hexlet.io\n   '
                'proxy: 123.234.53.22\n   timeout: 50\n}')

    result = generate_diff(file1, file2)
    assert result == expected


def test_data_load(tmp_path):
    file1 = get_path('file1.json')
    expected = {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22',
                'timeout': 50}
    result = data_load(file1)
    assert result == expected
