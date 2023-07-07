# gendiff.py

import argparse
from gendiff.tools import generate_diff
from gendiff.formater import stylish


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference.",
        usage="%(prog)s [-h] [-f FORMAT] first_file second_file",
    )
    parser.add_argument("first_file", help="First configuration file")
    parser.add_argument("second_file", help="Second configuration file")
    parser.add_argument("-f", "--format", help="set format of output", default="stylish")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Access the values passed for file_path1 and file_path2
    file_path1 = args.first_file
    file_path2 = args.second_file
    format_option = args.format

    # Perform operations
    diff = generate_diff(file_path1, file_path2)
    if format_option == "stylish":
        print(stylish(diff))
    else:
        print(diff)
        pass

if __name__ == "__main__":
    main()
