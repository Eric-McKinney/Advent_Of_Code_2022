import sys
import unittest
import day10
import pprint


class MyTestCase(unittest.TestCase):
    def test_part1(self):
        with open("test_input.txt", "r") as f:
            data = f.readlines()

        circuit = day10.ClockCircuit()
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

        pprint.pprint(circuit.cycle_log)
        signal_strength_sum = 0
        for cycle in range(20, 260, 40):
            signal_strength = day10.calculate_signal_strength(circuit, cycle)
            signal_strength_sum += signal_strength
            # print(f"{cycle = }\t\t{signal_strength = }")

        self.assertEqual(13140, signal_strength_sum)


if __name__ == '__main__':
    unittest.main()
