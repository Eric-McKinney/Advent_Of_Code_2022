import sys


class ClockCircuit:
    def __init__(self):
        self.clock_cycle = 1
        self.x = 1
        self.cycle_log = {1: 1}

        # part 2 stuff
        # crt is 40 wide and 6 high
        # starts at pixel 0
        self.crt_image = ""
        self.__update_crt_image()

    def __update_clock(self):
        self.clock_cycle += 1
        self.cycle_log[self.clock_cycle] = self.x

        self.__update_crt_image()

    def noop(self):
        self.__update_clock()

    def add_x(self, x: int):
        self.__update_clock()

        self.x += x
        self.__update_clock()

    def __create_line_with_sprite(self) -> str:
        # bounds are 0 and 40, but sprite is three wide with self.x at center, so bounds for visible sprite become +/- 1
        if self.x > 41 or self.x < -1:
            return "." * 40

        line = ""
        sprite_coordinates = [self.x - 1, self.x, self.x + 1]
        for idx in range(40):
            if idx in sprite_coordinates:
                line += "#"
            else:
                line += "."

        return line

    def __update_crt_image(self):
        line = self.__create_line_with_sprite()

        line_idx = (self.clock_cycle % 40) - 1
        self.crt_image += line[line_idx]

        if self.clock_cycle % 40 == 0:
            self.crt_image += "\n"


def calculate_signal_strength(circuit: ClockCircuit, cycle: int):
    x = circuit.cycle_log[cycle]
    return cycle * x


def parse_input() -> ClockCircuit:
    with open("input.txt", "r") as f:
        data = f.readlines()

    circuit = ClockCircuit()
    for line in data:
        line = line.split()

        operation = line[0]

        match operation:
            case "noop":
                circuit.noop()
            case "addx":
                x = int(line[1])
                circuit.add_x(x)
            case _:
                print(f'Operation "{operation}" not recognized', file=sys.stderr)

    return circuit


def part1():
    circuit = parse_input()

    signal_strength_sum = 0
    for cycle in range(20, 260, 40): # gets 20th, 60th, 100th, ..., 220th cycles
        signal_strength_sum += calculate_signal_strength(circuit, cycle)

    print(signal_strength_sum)


def part2():
    circuit = parse_input()

    print(circuit.crt_image)


if __name__ == "__main__":
    # part1()
    part2()
