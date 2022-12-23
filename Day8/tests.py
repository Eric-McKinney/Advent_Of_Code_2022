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

    def test_count_visible1(self):
        test_input = ["13536", "34243"]

        output1 = day8.count_visible_trees_left(test_input, 0, 0, "1")
        output2 = day8.count_visible_trees_left(test_input, 0, 1, "3")
        output3 = day8.count_visible_trees_left(test_input, 1, 3, "4")

        self.assertEqual(0, output1)
        self.assertEqual(1, output2)
        self.assertEqual(2, output3)

    def test_part2(self):
        with open("test_input2.txt", "r") as f:
            data = f.read()
            data = data.strip()
            data = data.split("\n")

        tree_scenic_scores = {}

        for row in range(len(data)):
            for col in range(len(data[row])):
                height = data[row][col]
                trees_visible_left = day8.count_visible_trees_left(data, row, col, height)
                trees_visible_right = day8.count_visible_trees_right(data, row, col, height)
                trees_visible_top = day8.count_visible_trees_top(data, row, col, height)
                trees_visible_bottom = day8.count_visible_trees_bottom(data, row, col, height)

                scenic_score = day8.calculate_scenic_score(trees_visible_left, trees_visible_right, trees_visible_top,
                                                      trees_visible_bottom)
                tree_scenic_scores[(row, col)] = scenic_score

        max_scenic_score = max(tree_scenic_scores.values())
        self.assertEqual(8, max_scenic_score)


if __name__ == '__main__':
    unittest.main()
