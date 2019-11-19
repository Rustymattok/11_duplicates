import os
import argparse


def get_link_files(folder_path):
    folder = []
    for info_walk in os.walk(folder_path):
        folder.append(info_walk)
    return folder


def optimize_memory(folder):
    file_list_original = []
    for address, dirs, files in folder:
        for file in files:
            if file in file_list_original:
                file_path_remove = address+'/'+file
                if os.path.isfile(file_path_remove):
                    os.remove(file_path_remove)
                    print('File: ', file_path_remove, ' was removed')
                else:
                    print('Error: %s file not found: ', file_path_remove)
            else:
                file_list_original.append(file)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--folder',
        required=True,
        help='command - folder for scan and clean'
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    try:
        folder_path = args.folder
        optimize_memory(get_link_files(folder_path))
    except ValueError:
        print('not correct format')


if __name__ == '__main__':
    main()
