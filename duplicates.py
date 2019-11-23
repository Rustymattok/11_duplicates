import os
import argparse


def get_path_list(folder_path):
    path_list = []
    if not os.path.exists(folder_path):
        print("not exist directory")
        return None
    for info_walk in os.walk(folder_path):
        path_list.append(info_walk)
    return path_list


def show_path_files(files_path):
    if files_path is None:
        print('no directory for scan')
        return
    for file_path in files_path:
        if os.path.isfile(file_path):
            print('Patch to duplicate file: ' + file_path)


def get_duplicate_files(folder):
    duplicate_files = []
    if folder is None:
        return
    file_list_original = []
    for address, dirs, files_path in folder:
        for file_path in files_path:
            if file_path in file_list_original:
                file_path_duplicate = os.path.join(address, file_path)
                duplicate_files.append(file_path_duplicate)
            else:
                file_list_original.append(file_path)
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
    duplicate_files = get_duplicate_files(get_path_list(folder_path))
    show_path_files(duplicate_files)


if __name__ == '__main__':
    main()
