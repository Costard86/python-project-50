from gendiff.cli import parse_args
from gendiff.generate_diff import generate_diff


def main():
    first_file, second_file, format_data = parse_args()
    diff = generate_diff(first_file, second_file, format_data)
    print(diff)


if __name__ == '__main__':
    main()
