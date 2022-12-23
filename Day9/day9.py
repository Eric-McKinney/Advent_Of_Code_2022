
class Rope:
    def __init__(self):
        self.__head_x = 0
        self.__head_y = 0
        self.__tail_x = 0
        self.__tail_y = 0
        self.coordinates_tail_visited = {(0, 0)}

    def move_head(self, direction, num_of_moves):
        for _ in range(num_of_moves):
            match direction:
                case "L":
                    self.__head_x -= 1
                case "R":
                    self.__head_x += 1
                case "U":
                    self.__head_y += 1
                case "D":
                    self.__head_y -= 1
                case _:
                    print(f"Direction '{direction}' not recognized")

            self.__move_tail()

    def __move_tail(self):
        x_diff = self.__head_x - self.__tail_x
        y_diff = self.__head_y - self.__tail_y

        if abs(x_diff) <= 1 and abs(y_diff) <= 1:
            return

        if x_diff != 0:
            self.__tail_x += x_diff/abs(x_diff) # always 1, but keeps sign

        if y_diff != 0:
            self.__tail_y += y_diff/abs(y_diff)

        self.coordinates_tail_visited.add((self.__tail_x, self.__tail_y))


def part1():
    with open("input.txt", "r") as f:
        data = f.readlines()

    rope = Rope()
    for line in data:
        line = line.split()

        direction = line[0]
        num_of_moves = int(line[1])

        rope.move_head(direction, num_of_moves)

    num_coordinates_tail_visited = len(rope.coordinates_tail_visited)
    print(num_coordinates_tail_visited)


if __name__ == "__main__":
    part1()
