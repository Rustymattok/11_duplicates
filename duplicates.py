import os
import argparse
from collections import defaultdict


def get_path_list(folder_path):
    path_list = []
    for info_walk in os.walk(folder_path):
        path_list.append(info_walk)
    return path_list


def show_path_files(files_location):
    for (file_name, files_path) in files_location.items():
        if len(files_path) > 1:
            for file_path in files_path:
                print('Patch to duplicate file: ', file_path)


def get_files_location(path_list):
    files_location = defaultdict(list)
    for address, dirs, files_path in path_list:
        for file_name in files_path:
            files_location[file_name].append(os.path.join(address, file_name))
    return files_location


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
        files_location = get_files_location(get_path_list(folder_path))
        show_path_files(files_location)
    else:
        print('not correct directory or not exist')


if __name__ == '__main__':
    main()
