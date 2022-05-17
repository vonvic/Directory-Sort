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

def get_extension(file: str) -> str:
    dot_index = len(file) - 1
    for char in reversed(file):
        if char == '.':
            break
        dot_index -= 1
    return "unknown" if dot_index < 0 else file[dot_index+1:]
        
def create_dir(name: str) -> None:
    if not os.path.isdir(name):
        os.mkdir(name)

def move_file(source: str, destination: str):
    os.rename(source, destination)

def sort(directory: str) -> None:
    print("Sorting...", end='')
    
    for file in os.listdir(directory):
        full_path_to_file = directory + file
        if os.path.isfile(full_path_to_file):
            extension = get_extension(file)
            new_location = f'{directory}{extension}/{file}'
            create_dir(directory + extension)
            move_file(full_path_to_file, new_location)

    print("Done!")

if __name__ == '__main__':
    directory = request_directory()
    sort(directory)