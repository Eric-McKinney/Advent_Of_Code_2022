
def main():
    with open("input.txt", "r") as f:
        data = f.readlines()

    visible_trees = len(data)*2 + (len(data[0]) - 2)*2 # edges of grid
    for line in data[1:-1]:
        pass


if __name__ == "__main__":
    main()
