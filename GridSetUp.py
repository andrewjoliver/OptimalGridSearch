import random


class GridCell:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.down_expanded = True if self.x == n else False
        self.right_expanded = True if self.y == n else False


class GridCellInverted:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.up_expanded = True if self.x == 0 else False
        self.left_expanded = True if self.y == 0 else False


def generate_grid(n, max_range):
    my_grid = []
    for x in range(0, n):
        grid_row = []
        for y in range(0, n):
            grid_row.append(random.randrange(1, max_range))
        my_grid.append(grid_row)

    return my_grid


def print_grid(grid):
    for x in range(0, len(grid)):
        print(grid[x])


def main():
    n = 5
    grid = generate_grid(n)
    print_grid(grid)


if __name__ == '__main__':
    main()