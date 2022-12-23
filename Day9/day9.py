
class Rope:
    def __init__(self):
        self.__head = [0, 0]
        self.__tail = [0, 0]


def part1():
    with open("input.txt", "r") as f:
        data = f.readlines()

    for line in data:
        line = line.split()


if __name__ == "__main__":
    part1()
