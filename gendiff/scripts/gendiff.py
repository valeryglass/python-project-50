# gendiff.py

import argparse
from gendiff.tools import load_data, compare_data, format_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
        usage="%(prog)s [-h] [-f FORMAT] first_file second_file",
    )
    parser.add_argument("first_file", help="First configuration file")
    parser.add_argument("second_file", help="Second configuration file")
    parser.add_argument("-f", "--format", help="set format of output")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values passed for file_path1 and file_path2
    file_path1 = args.first_file
    file_path2 = args.second_file
    # format_option = args.format

    # Perform operations
    diff = generate_diff(file_path1, file_path2)
    print(format_diff(diff, " ", 4))


def generate_diff(file_path1, file_path2):
    """
    Compare two YAML/JSON files and return a string with the differences
    """
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)

    diff = compare_data(data1, data2)
    # sorted_diff = sort_diff_keys(diff)
    # result = format_diff(diff, ' ', 4)

    return diff


if __name__ == "__main__":
    main()
