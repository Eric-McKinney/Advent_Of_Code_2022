import sys


class ClockCircuit:
    def __init__(self):
        self.clock_cycle = 1
        self.x = 1
        self.cycle_log = {1: 1}

    def __update_clock(self):
        self.clock_cycle += 1
        self.cycle_log[self.clock_cycle] = self.x

    def noop(self):
        self.__update_clock()

    def add_x(self, x: int):
        self.__update_clock()

        self.x += x
        self.__update_clock()


def calculate_signal_strength(circuit: ClockCircuit, cycle: int):
    x = circuit.cycle_log[cycle]
    return cycle * x


def part1():
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

    signal_strength_sum = 0
    for cycle in range(20, 260, 40): # gets 20th, 60th, 100th, ..., 220th cycles
        signal_strength_sum += calculate_signal_strength(circuit, cycle)

    print(signal_strength_sum)


if __name__ == "__main__":
    part1()
