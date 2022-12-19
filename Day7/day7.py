import pprint

def path_to_string(path: list) -> str:
    path_string = ""
    for directory_name in path:
        path_string += f"/{directory_name}"

    return path_string


class FileSystem:
    def __init__(self):
        self.file_system = {"/": {}}
        self.curr_directory = None
        self.curr_directory_path = ""

    def __align_curr_directory_to_path(self, path: list) -> None:
        self.curr_directory = self.file_system["/"]
        for directory in path:
            self.curr_directory = self.curr_directory[directory]

    def change_dir(self, directory_name: str) -> None:
        if self.curr_directory_path == "/":
            path = []
            # this is the fun exception to the rule I made. If the path is only "/" then splitting it returns ['', '']
            # where for anything else it would be ['', 'dir1', 'dir2', ...]
        else:
            path = self.curr_directory_path.split("/")
            # makes base directory "/" an empty string in the list
            # so here's the bandaid fix:
            path.pop(0)

        if directory_name == "..":
            path.pop()
            self.curr_directory_path = path_to_string(path)
            self.__align_curr_directory_to_path(path)
        elif directory_name == "/":
            path = []
            self.curr_directory_path = ""
            self.__align_curr_directory_to_path(path)
        else:
            self.curr_directory_path += f"/{directory_name}"
            self.curr_directory = self.curr_directory[directory_name]

    def add_dir(self, dir_name: str) -> None:
        if dir_name not in self.curr_directory.keys():
            self.curr_directory[dir_name] = {}

    def add_file(self, file_name: str, file_size: int) -> None:
        self.curr_directory[file_name] = file_size


def parse_input(data: list) -> dict:
    file_system = FileSystem()
    for line in data:
        line = line.split()
        if line[0] == "$":
            command = line[1]

            match command:
                case "cd":
                    dir_name = line[2]
                    file_system.change_dir(dir_name)
                case "ls":
                    pass
                case _:
                    print(f"Unhandled case: {command}\nFrom {line = }")
                    break
        else:
            if line[0] == "dir":
                dir_name = line[1]
                file_system.add_dir(dir_name)
            else:
                file_size = int(line[0])
                file_name = line[1]
                file_system.add_file(file_name, file_size)

    return file_system.file_system


def get_directory_size(directory_name: str, directory: dict, max_size: int, directories_small_enough: dict) -> int:
    sub_directories = []
    directory_size = 0

    for name in list(directory.keys()): # needs to be list or everything is a dictionary
        contents = directory[name]
        if type(contents) is dict:
            sub_directories.append([name, contents])
        elif type(contents) is int:
            directory_size += contents
        else:
            print(f"Dunno how, but {contents} is not int or dict")

    for sub_directory in sub_directories:
        name = sub_directory[0]
        contents = sub_directory[1]
        directory_size += get_directory_size(name, contents, max_size, directories_small_enough)

    if directory_size <= max_size:
        directories_small_enough[directory_name] = directory_size

    return directory_size


def main():
    MAX_SIZE = 100_000

    with open("input.txt", "r") as f:
        data = f.readlines()

    parsed_input = parse_input(data)
    # pprint.pprint(parsed_input.file_system)

    directories_small_enough = {}
    get_directory_size("/", parsed_input, MAX_SIZE, directories_small_enough)

    size_sum = 0
    for size in directories_small_enough.values():
        size_sum += size

    print(size_sum)


if __name__ == "__main__":
    main()
