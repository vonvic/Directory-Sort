import os

def directory_input() -> str:
    directory = input("Enter which directory to sort (`.` for the current directory or CTRL+D to quit): ")

    if directory[0] == '~':
        directory = os.path.expanduser('~') + directory[1:]

    if directory[-1] != '/':
        directory += '/'
    
    return directory

def request_directory() -> str:
    directory = directory_input()
    valid_directory = os.path.isdir(directory)

    while not valid_directory:
        print("ERROR: Invalid directory")
        directory = directory_input()
        valid_directory = os.path.isdir(directory)

    return directory


def sort(directory: str) -> None:
    print("Sorting...", end='')
    
    for file in os.listdir(directory):
        print(file)

    print("Done!")

if __name__ == '__main__':
    directory = request_directory()
    sort(directory)