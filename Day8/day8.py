
def is_visible_from_left(grid: list, row: int, col: int) -> bool:
    height = grid[row][col]
    for tree_height in grid[row][: col]:
        if tree_height >= height:
            return False

    return True


def is_visible_from_right(grid: list, row: int, col: int) -> bool:
    height = grid[row][col]
    for tree_height in grid[row][col + 1: ]:
        if tree_height >= height:
            return False

    return True


def is_visible_from_top(grid: list, row: int, col: int) -> bool:
    height = grid[row][col]
    for trees in grid[: row]:
        tree_height = trees[col]

        if tree_height >= height:
            return False

    return True


def is_visible_from_bottom(grid: list, row: int, col: int) -> bool:
    height = grid[row][col]
    for trees in grid[row + 1: ]:
        tree_height = trees[col]

        if tree_height >= height:
            return False

    return True


def is_edge(grid: list, row: int, col: int) -> bool:
    return row == 0 or col == 0 or row == len(grid) - 1 or col == len(grid[row]) - 1


def main():
    with open("input.txt", "r") as f:
        data = f.readlines()

    num_of_visible_trees = 0

    for row in range(len(data)):
        for col in range(len(data[row])):
            if is_edge(data, row, col) or \
               is_visible_from_left(data, row, col) or \
               is_visible_from_right(data, row, col) or \
               is_visible_from_top(data, row, col) or \
               is_visible_from_bottom(data, row, col):

                num_of_visible_trees += 1

    print(num_of_visible_trees)




if __name__ == "__main__":
    main()
