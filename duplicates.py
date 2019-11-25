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


def get_duplicate_files(folder):
    duplicate_files = []
    d = defaultdict(int)
    for address, dirs, files_path in folder:
        for file_name_path in files_path:
            if d[file_name_path] > 0:
                file_path_duplicate = os.path.join(address, file_name_path)
                duplicate_files.append(file_path_duplicate)
            d[file_name_path] += 1
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
