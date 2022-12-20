import pprint


MAX_SIZE = 100_000
TOTAL_SPACE = 70_000_000
MIN_UNUSED_SPACE = 30_000_000


def path_to_string(path: list) -> str:
    path_string = ""
    for directory_name in path:
        path_string += f"/{directory_name}"

    return path_string


class FileSystem:
    def __init__(self):
        self.file_system = {"/": {}}
        self.path = []

    def get_curr_directory(self) -> dict:
        curr_directory = self.file_system
        for directory in self.path:
            curr_directory = curr_directory[directory]

        return curr_directory

    def change_dir(self, directory_name: str) -> None:
        if directory_name == "/":
            self.path = ["/"]
            return

        if directory_name == "..":
            self.path.pop()
        else:
            self.path.append(directory_name)

    def add_dir(self, dir_name: str) -> None:
        curr_directory = self.get_curr_directory()

        if dir_name not in curr_directory.keys():
            curr_directory[dir_name] = {}

    def add_file(self, file_name: str, file_size: int) -> None:
        curr_directory = self.get_curr_directory()
        curr_directory[file_name] = file_size


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
                    pass # not supposed to do anything, just here to show this case is covered
                case _:
                    print(f"Unhandled case: {command}\nFrom {line = }")
                    break
        else:
            if line[0] == "dir":
                dir_name = line[1]
                file_system.add_dir(dir_name)
            elif line[0].isdigit():
                file_size = int(line[0])
                file_name = line[1]
                file_system.add_file(file_name, file_size)
            else:
                print("Not file or directory")

    return file_system.file_system


def get_directory_size(directory_name: str, directory: dict, max_size: int, directories_small_enough: list) -> int:
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

    # if directory_size <= max_size:
    #     directories_small_enough.append([directory_name, directory_size]) # originally was dict, but duplicate
    #                                                                       # directory names are a thing
    directories_small_enough.append([directory_name, directory_size])
    return directory_size


def find_smallest_to_delete(directories: list, min_size: int) -> int:
    candidates = []
    for name, size in directories:
        if size >= min_size:
            candidates.append(size)

    candidates.sort()
    return candidates[0]


def main():
    with open("input.txt", "r") as f:
        data = f.readlines()

    parsed_input = parse_input(data)
    # pprint.pprint(parsed_input)

    directories_small_enough = []
    get_directory_size("/", parsed_input["/"], MAX_SIZE, directories_small_enough)

    # pprint.pprint(directories_small_enough)

    # size_sum = 0
    # for directory in directories_small_enough:
    #     size_sum += directory[1]
    #
    # print(f"{size_sum = }")

    root_dir_size = 43313415
    current_unused_space = TOTAL_SPACE - root_dir_size
    min_size_to_delete = MIN_UNUSED_SPACE - current_unused_space
    
    size = find_smallest_to_delete(directories_small_enough, min_size_to_delete)
    print(f"{size = }")


if __name__ == "__main__":
    main()
