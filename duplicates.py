import os
import argparse
from collections import defaultdict


def get_path_list(folder_path):
    path_list = []
    for info_walk in os.walk(folder_path):
        path_list.append(info_walk)
    return path_list


def show_path_files(files_path):
    for file_path in files_path:
        if os.path.isfile(file_path):
            print('Patch to duplicate file: ' + file_path)


def get_duplicate_files(path_list):
    duplicate_files = []
    files_location = defaultdict(list)
    for address, dirs, files_path in path_list:
        for file_name_path in files_path:
            if file_name_path in files_location:
                duplicate_files.append(address + '/' + file_name_path)
            else:
                files_location[file_name_path] = address + '/' + file_name_path
    return duplicate_files


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--directory',
        required=True,
        help='command - directory for scan and clean'
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    folder_path = args.directory
    if os.path.isdir(folder_path):
        duplicate_files = get_duplicate_files(get_path_list(folder_path))
        show_path_files(duplicate_files)
    else:
        print('not correct directory or not exist')


if __name__ == '__main__':
    main()
