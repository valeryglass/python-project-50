# gendiff.py


import argparse
import json


def main():
    parser = argparse.ArgumentParser(
            description='Compares two configuration files'
            ' and shows a difference.',
            usage='%(prog)s [-h] [-f FORMAT] first_file second_file'
    )
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    parser.add_argument('-f', '--format', help='set format of output')
    # Parse the command-line arguments
    args = parser.parse_args()
    # Access the values passed for file_path1 and file_path2
    file_path1 = args.first_file
    file_path2 = args.second_file
    # format_option = args.format
    # Perform operations
    diff = generate_diff(file_path1, file_path2)
    print(diff)




def generate_diff(file_path1, file_path2):
    '''
    Compare two JSON files and return a string with the differences
    '''
    with open(file_path1) as file1, open(file_path2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)

    diff = compare_data(data1, data2)
    sorted_diff = sort_diff_keys(diff)
    result = format_diff(sorted_diff)

    return f"{{\n{result}\n}}"

def compare_data(data1, data2):
    removed = (('- ' + key, data1[key]) for key in data1 if key not in data2)
    modified_old = (('- ' + key, data1[key]) for key in data1 if key in data2 and data1[key] != data2[key])
    modified_new = (('+ ' + key, data2[key]) for key in data1 if key in data2 and data1[key] != data2[key])
    same = (('  ' + key, data1[key]) for key in data1 if key in data2 and data1[key] == data2[key])
    added = (('+ ' + key, data2[key]) for key in data2 if key not in data1)
    diff = dict(chain(removed, modified_old, modified_new, same, added))
    return diff


def sort_diff_keys(diff):
    return dict(sorted(diff.items(), key=lambda x: x[0][2]))


def format_diff(sorted_diff):
    return "\n".join([f"{key}: {value}" for key, value in sorted_diff.items()])


if __name__ == '__main__':
    main()
