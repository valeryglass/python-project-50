# gendiff.py


import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.', usage='%(prog)s [-h] [-f FORMAT] first_file second_file')
    parser.add_argument('first_file', help='First configuration file')
    parser.add_argument('second_file', help='Second configuration file')
    parser.add_argument('-f FORMAT', '--format FORMAT', help='set format of output')


    # Parse the command-line arguments
    args = parser.parse_args()


    # Access the values passed for first_file and second_file
    # first_file = args.first_file
    # second_file = args.second_file
    # format_option = args.format
   
    # Perform the necessary operations based on the provided arguments
    #------- Add your code logic here-------------


    # Example: Print the file names
    # print(f'First File: {first_file}')
    # print(f'Second File: {second_file}')
    # print(f'Format: {format_option}')
   
if __name__ == '__main__':
    main()
