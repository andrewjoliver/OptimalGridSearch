from GridSetUp import generate_grid, print_grid
from Printers import print_path


def find_path_recursive(grid, x, y, path, val):
    if x == len(grid) - 1 and y == len(grid) - 1:
        return val, path
    elif x == len(grid) - 1:
        return find_path_recursive(grid, x, y+1, path+"R", val+grid[x][y+1])
    elif y == len(grid) - 1:
        return find_path_recursive(grid, x+1, y, path+"D", val+grid[x+1][y])
    else:
        down = find_path_recursive(grid, x+1, y, path+"D", val+grid[x+1][y])
        right = find_path_recursive(grid, x, y+1, path+"R", val+grid[x][y+1])

        if down[0] > right[0]:
            return down
        else:
            return right


def main():
    n = 5
    main_grid = generate_grid(n, 100)
    val, path = find_path_recursive(main_grid, 0, 0, "", main_grid[0][0])
    print_grid(main_grid)
    print("--------")
    print(val)
    print_path(path)


if __name__ == "__main__":
    main()
