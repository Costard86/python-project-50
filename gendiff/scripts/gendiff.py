import argparse
from gendiff.fuctions.generate_diff import generate_diff
from gendiff.formatters.stylish import format_stylish


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration '
                                                 'files and shows a '
                                                 'difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output', default='stylish')

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    if args.format == 'stylish':
        print(format_stylish(diff))

    else:
        print(diff)


if __name__ == '__main__':
    main()
