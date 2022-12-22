import unittest
import day8


class MyTestCase(unittest.TestCase):
    def test_part1(self):
        with open("test_input.txt", "r") as f:
            data = f.readlines()

        num_of_visible_trees = 0

        for row in range(len(data)):
            for col in range(len(data[row]) - 1):
                height = data[row][col]
                if day8.is_edge(data, row, col) or \
                   day8.is_visible_from_left(data, row, col, height) or \
                   day8.is_visible_from_right(data, row, col, height) or \
                   day8.is_visible_from_top(data, row, col, height) or \
                   day8.is_visible_from_bottom(data, row, col, height):

                    num_of_visible_trees += 1

        self.assertEqual(21, num_of_visible_trees)


if __name__ == '__main__':
    unittest.main()
