def main():
    with open("input.txt", "r") as f:
        data = f.readlines()

    file_system = {}
    for line in data:
        if line[1] == "$":
            line.split()
            command = line[1]

            match command:
                case "cd":
                    directory = line[2]
                case "ls":
                    pass


if __name__ == "__main__":
    main()
