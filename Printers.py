def print_stack(grid):
    print("[", end=" ")
    for cell in grid:
        print("(" + str(cell.x) + "," + str(cell.y) + ")", end="")
    print(" ]")


def print_map(map_val):
    for key in map_val:
        print(key)


def print_cell(cell):
    print("(" + str(cell.x) + ", " + str(cell.y) + ")")


def print_path(path):
    for move in path:
        print(move, end="")
    print("\n", end="")