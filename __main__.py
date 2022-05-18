# Author: Cayas, Von Vic
# Date: Tue May 17, 2022
# Description: Requests the user for a directory and sorts that directory.

import os, sys, signal

def directory_input() -> str:
    '''Returns directory received by the user. Always returns directory path
    terminated by the forward slash '/' character. Also, expands the `~` as the
    home directory.'''

    directory = input("Enter which directory to sort (`.` for the current directory or `CTRL+C` to quit): ")

    if directory[0] == '~':
        directory = os.path.expanduser('~') + directory[1:]

    if directory[-1] != '/':
        directory += '/'
    
    return directory

def request_directory() -> str:
    '''Returns a valid user directory.'''
    directory = directory_input()
    valid_directory = os.path.isdir(directory)

    while not valid_directory:
        print("ERROR: Invalid directory")
        directory = directory_input()
        valid_directory = os.path.isdir(directory)

    return directory

def get_extension(file: str) -> str:
    '''Returns the extension of `file`. If no extension is found, then returns
    "unknown".'''
    dot_index = len(file) - 1
    for char in reversed(file):
        if char == '.':
            break
        dot_index -= 1
    return "unknown" if dot_index < 0 else file[dot_index+1:]

def create_dir(name: str) -> None:
    '''Creates a directory if it doesn't already exist'''
    if not os.path.isdir(name):
        os.mkdir(name)

def sort(directory: str) -> None:
    '''Iterates through every file immediately in `directory` and moves into a
    a folder (inside that directory) with the name of that extension.'''
    print("Sorting...", end='')

    for file in os.listdir(directory):
        full_path_to_file = directory + file
        if os.path.isfile(full_path_to_file):
            extension = get_extension(file)
            new_location = f'{directory}{extension}/{file}'
            create_dir(directory + extension)
            os.rename(full_path_to_file, new_location)

    print("Done!")

if __name__ == '__main__':
    signal.signal(signal.SIGINT, lambda _a, _b: sys.exit())
    directory = request_directory()
    sort(directory)