def path_to_string(path: list) -> str:
    path_string = ""
    for directory_name in path:
        path_string += f"/{directory_name}"

    return path_string


class FileSystem:
    def __init__(self):
        self.file_system = {}
        self.curr_directory = None
        self.curr_directory_path = ""

    def change_dir(self, directory_name: str) -> None:
        path = self.curr_directory_path.split("/")

        if directory_name == "..":
            path.pop()
            self.curr_directory_path = path_to_string(path)
        elif directory_name not in path:
            self.curr_directory_path += f"/{directory_name}"
        else:
            directory_idx = path.index(directory_name)
            path = path[: directory_idx + 1]
            self.curr_directory_path = path_to_string(path)

    def add_dir(self, dir_name: str) -> None:
        if dir_name not in self.file_system[self.curr_directory].keys():
            self.file_system[self.curr_directory][dir_name] = {}

    def add_file(self, file_name: str, file_size: int) -> None:
        self.curr_directory[file_name] = file_size


def main():
    with open("input.txt", "r") as f:
        data = f.readlines()

    file_system = FileSystem()
    for line in data:
        line.split()
        if line[0] == "$":
            command = line[1]

            match command:
                case "cd":
                    dir_name = line[1]
                    file_system.change_dir(dir_name)
                case "ls":
                    continue
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


if __name__ == "__main__":
    main()
