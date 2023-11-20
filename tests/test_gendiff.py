from pathlib import Path
from gendiff.fuctions.generate_diff import generate_diff
from gendiff.fuctions.generate_diff import data_load
from gendiff.formatters.stylish import format_stylish


def get_path(file_name):
    p = Path(__file__)
    tests = p.absolute().parent
    return tests/'fixtures'/file_name


def test_merge(tmp_path):
    file1 = get_path('file1.json')
    file2 = get_path('file2.json')
    expected = ('{\n- follow: false\n  host: hexlet.io\n'
                '- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n'
                '+ verbose: true\n}')

    result = format_stylish(generate_diff(file1, file2))
    assert result == expected


def test_merge_yml_json(tmp_path):
    file1 = get_path('filepath1.yml')
    file2 = get_path('file2.json')
    expected = ('{\n- follow: false\n  host: hexlet.io\n'
                '- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n'
                '+ verbose: true\n}')

    result = format_stylish(generate_diff(file1, file2))
    assert result == expected


def test_merge_same_text(tmp_path):
    file1 = get_path('file1.json')
    file2 = get_path('file3.json')
    expected = ('{\n  follow: false\n  host: hexlet.io\n  '
                'proxy: 123.234.53.22\n  timeout: 50\n}')

    result = format_stylish(generate_diff(file1, file2))
    assert result == expected


def test_merge_same_text_yml_json(tmp_path):
    file1 = get_path('filepath1.yml')
    file2 = get_path('file1.json')
    expected = ('{\n  follow: false\n  host: hexlet.io\n  '
                'proxy: 123.234.53.22\n  timeout: 50\n}')

    result = format_stylish(generate_diff(file1, file2))
    assert result == expected


def test_data_load(tmp_path):
    file1 = get_path('file1.json')
    expected = {'follow': False, 'host': 'hexlet.io', 'proxy': '123.234.53.22',
                'timeout': 50}
    result = data_load(file1)
    assert result == expected


def test_format_stylish(tmp_path):
    file1 = get_path('file1.yaml')
    file2 = get_path('file2.yaml')

    diff = generate_diff(file1, file2)
    expected_output = '''{
  common: {
    + follow: false
      setting1: Value 1
    - setting2: 200
    - setting3: true
    + setting3: null
    + setting4: blah blah
    + setting5: {
        key5: value5
    }
      setting6: {
          doge: {
            - wow: 
            + wow: so much
        }
          key: value
        + ops: vops
    }
}
  group1: {
    - baz: bas
    + baz: bars
      foo: bar
    - nest: {
        key: value
    }
    + nest: str
}
- group2: {
    abc: 12345
    deep: {
        id: 45
    }
}
+ group3: {
    deep: {
        id: {
            number: 45
        }
    }
    fee: 100500
}
}'''

    assert format_stylish(diff) == expected_output


