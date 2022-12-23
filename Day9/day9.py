
class Rope:
    def __init__(self):
        self.__head = [0, 0]
        self.__tail = [0, 0]
        self.coordinates_tail_visited = {[0, 0]}

    def move_head(self, direction, num_of_moves):
        for _ in range(num_of_moves):
            match direction:
                case "L":
                    self.__head[0] -= 1
                case "R":
                    self.__head[0] += 1
                case "U":
                    self.__head[1] += 1
                case "D":
                    self.__head[1] -= 1
                case _:
                    print(f"Direction '{direction}' not recognized")

            self.__move_tail()

    def __move_tail(self):
        pass


def part1():
    with open("input.txt", "r") as f:
        data = f.readlines()

    rope = Rope()
    for line in data:
        line = line.split()

        direction = line[0]
        num_of_moves = line[1]

        rope.move_head(direction, num_of_moves)


if __name__ == "__main__":
    part1()
