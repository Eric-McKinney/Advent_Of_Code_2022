
def is_visible_from_left(grid: list, row: int, col: int, height: str) -> bool:
    for tree_height in grid[row][: col]:
        if tree_height >= height:
            return False

    return True


def is_visible_from_right(grid: list, row: int, col: int, height: str) -> bool:
    for tree_height in grid[row][col + 1: ]:
        if tree_height >= height:
            return False

    return True


def is_visible_from_top(grid: list, row: int, col: int, height: str) -> bool:
    for trees in grid[: row]:
        tree_height = trees[col]

        if tree_height >= height:
            return False

    return True


def is_visible_from_bottom(grid: list, row: int, col: int, height: str) -> bool:
    for trees in grid[row + 1: ]:
        tree_height = trees[col]

        if tree_height >= height:
            return False

    return True


def is_edge(grid: list, row: int, col: int) -> bool:
    return row == 0 or col == 0 or row == len(grid) - 1 or col == len(grid[row]) - 1


def part1():
    with open("input.txt", "r") as f:
        data = f.readlines()

    num_of_visible_trees = 0

    for row in range(len(data)):
        for col in range(len(data[row]) - 1):
            height = data[row][col]
            if is_edge(data, row, col) or \
               is_visible_from_left(data, row, col, height) or \
               is_visible_from_right(data, row, col, height) or \
               is_visible_from_top(data, row, col, height) or \
               is_visible_from_bottom(data, row, col, height):

                num_of_visible_trees += 1

    print(num_of_visible_trees)


def calculate_scenic_score(trees_visible_left: int, trees_visible_right: int, trees_visible_top: int, trees_visible_bottom: int) -> int:
    return trees_visible_left * trees_visible_right * trees_visible_top * trees_visible_bottom


def count_visible_trees_left(grid: list, row: int, col: int, height: str) -> int:
    visible_trees = 0

    if col == 0:
        return visible_trees

    for tree_height in grid[row][col - 1: : -1]:
        visible_trees += 1

        if tree_height >= height:
            return visible_trees

    return visible_trees


def count_visible_trees_right(grid:list, row: int, col: int, height: str) -> int:
    visible_trees = 0
    for tree_height in grid[row][col + 1: ]:
        visible_trees += 1

        if tree_height >= height:
            return visible_trees

    return visible_trees


def count_visible_trees_top(grid:list, row: int, col: int, height: str) -> int:
    visible_trees = 0

    if row == 0:
        return visible_trees

    for trees in grid[row - 1: : -1]:
        visible_trees += 1

        tree_height = trees[col]
        if tree_height >= height:
            return visible_trees

    return visible_trees


def count_visible_trees_bottom(grid:list, row: int, col: int, height: str) -> int:
    visible_trees = 0
    for trees in grid[row + 1: ]:
        visible_trees += 1

        tree_height = trees[col]
        if tree_height >= height:
            return visible_trees

    return visible_trees


def part2():
    with open("input.txt", "r") as f:
        data = f.read()
        data = data.strip()
        data = data.split("\n")

    tree_scenic_scores = {}

    for row in range(len(data)):
        for col in range(len(data[row])):
            height = data[row][col]
            trees_visible_left = count_visible_trees_left(data, row, col, height)
            trees_visible_right = count_visible_trees_right(data, row, col, height)
            trees_visible_top = count_visible_trees_top(data, row, col, height)
            trees_visible_bottom = count_visible_trees_bottom(data, row, col, height)

            scenic_score = calculate_scenic_score(trees_visible_left, trees_visible_right, trees_visible_top, trees_visible_bottom)
            tree_scenic_scores[(row, col)] = scenic_score

    max_scenic_score = max(tree_scenic_scores.values())
    print(max_scenic_score)


if __name__ == "__main__":
    part1()
    part2()
