from GridSetUp import generate_grid
from Printers import print_map, print_path


def find_path_heuristic(grid):
    n = len(grid) - 1
    x, y = 0, 0
    path = ""
    sum_res = grid[0][0]

    while x < n or y < n:

        if y == n:
            x += 1
            path += "D"
            sum_res += grid[x][y]
            continue

        elif x == n:
            y += 1
            path += "R"
            sum_res += grid[x][y]
            continue

        else:
            right_sum = sum_row(grid, x, y, n, "right")
            down_sum = sum_row(grid, x, y, n, "down")

            if right_sum > down_sum:
                y += 1
                path += "R"
                sum_res += grid[x][y]

            else:
                x += 1
                path += "D"
                sum_res += grid[x][y]

    return sum_res, path


def sum_row(grid, x, y, n, sum_type):
    sum_res = 0
    num_cells = (n - y) if sum_type == "right" else (n - x)
    n += 1

    if sum_type == "right":
        y += 1
        for z in range(y, n):
            sum_res += grid[x][z]

    elif sum_type == "down":
        x += 1
        for x in range(x, n):
            sum_res += grid[x][y]

    return float(sum_res)/(num_cells)


if __name__ == '__main__':
    n = 20
    grid = generate_grid(n, 50)
    val, path = find_path_heuristic(grid)
    print_map(grid)
    print("----------")
    print(val)
    print_path(path)