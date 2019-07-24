from GridSetUp import GridCell, generate_grid
from Printers import print_map, print_path


def find_path_dfs(grid):
    n = len(grid) - 1
    my_stack = list()
    my_stack.append(GridCell(0, 0, n))

    best_val = 0
    curr_val = grid[0][0]
    best_path = list()
    curr_path = list()

    while len(my_stack) is not 0:
        cell = my_stack[-1]
        # print_stack(my_stack)

        if cell.down_expanded and cell.right_expanded:
            popped_cell = my_stack.pop()
            print(curr_path)
            if cell.x == n and cell.y == n:
                if curr_val > best_val:
                    best_val, best_path = curr_val, curr_path

            curr_val -= grid[popped_cell.x][popped_cell.y]
            curr_path = curr_path[:len(my_stack)-1]
            continue

        if cell.x < n and not cell.down_expanded:
            cell.down_expanded = True
            curr_val += grid[cell.x+1][cell.y]
            curr_path.append("D")
            my_stack.append(GridCell(cell.x+1, cell.y, n))

        elif cell.y < n and not cell.right_expanded:
            cell.right_expanded = True
            curr_val += grid[cell.x][cell.y+1]
            curr_path.append("R")
            my_stack.append(GridCell(cell.x, cell.y+1, n))

    return best_val, best_path


if __name__ == '__main__':
    n = 2
    grid = generate_grid(n, 100)
    val, path = find_path_dfs(grid)

    print_map(grid)
    print("-----")
    print(val)
    print_path(path)