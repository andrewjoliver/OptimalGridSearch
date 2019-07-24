import multiprocessing
from multiprocessing import Process
from GridSetUp import generate_grid
from Printers import print_map, print_path


class UpperGridCell:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.down_expanded = True if (self.x + self.y) == n else False
        self.right_expanded = True if (self.x + self.y) == n else False


class UpperInvertedGridCell:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.up_expanded = True if (self.x + self.y == n) else False
        self.left_expanded = True if (self.x + self.y == n) else False


def find_path_dfs_bidi_down(grid, return_dict):
    n = len(grid) - 1
    my_paths_and_vals = list()
    my_stack = list()
    my_stack.append(UpperGridCell(0, 0, n))

    curr_val = grid[0][0]
    curr_path = list()

    while len(my_stack) is not 0:
        cell = my_stack[-1]

        if cell.down_expanded and cell.right_expanded:
            popped_cell = my_stack.pop()
            if cell.x + cell.y == n:
                my_paths_and_vals.append((curr_path, curr_val, (str(cell.x) + " " + str(cell.y))))

            curr_val -= grid[popped_cell.x][popped_cell.y]
            curr_path = curr_path[:len(my_stack)-1]
            continue

        if cell.x < n and not cell.down_expanded:
            cell.down_expanded = True
            curr_val += grid[cell.x+1][cell.y]
            curr_path.append("D")
            my_stack.append(UpperGridCell(cell.x+1, cell.y, n))

        elif cell.y < n and not cell.right_expanded:
            cell.right_expanded = True
            curr_val += grid[cell.x][cell.y+1]
            curr_path.append("R")
            my_stack.append(UpperGridCell(cell.x, cell.y+1, n))

    return_dict.append(my_paths_and_vals)
    return my_paths_and_vals


def find_path_dfs_bidi_up(grid, return_dict):
    n = len(grid) - 1
    my_paths_and_vals = list()
    my_stack = list()
    my_stack.append(UpperInvertedGridCell(n, n, n))

    curr_val = grid[n][n]
    curr_path = list()

    while len(my_stack) is not 0:
        cell = my_stack[-1]

        if cell.up_expanded and cell.left_expanded:
            popped_cell = my_stack.pop()

            if cell.x + cell.y == n:
                my_paths_and_vals.append((curr_path, curr_val, (str(cell.x) + " " + str(cell.y))))

            curr_val -= grid[popped_cell.x][popped_cell.y]
            curr_path = curr_path[:len(my_stack)-1]
            continue

        if cell.x > 0 and not cell.up_expanded:
            cell.up_expanded = True
            curr_val += grid[cell.x-1][cell.y]
            curr_path.append("U")
            my_stack.append(UpperInvertedGridCell(cell.x-1, cell.y, n))

        elif cell.y > 0 and not cell.left_expanded:
            cell.left_expanded = True
            curr_val += grid[cell.x][cell.y-1]
            curr_path.append("L")
            my_stack.append(UpperInvertedGridCell(cell.x, cell.y-1, n))

    return_dict.append(my_paths_and_vals)
    return my_paths_and_vals


def resolve_bidi_paths(paths_down, paths_up, grid):
    max_val, max_path = 0, list()

    for path_down in paths_down:
        for path_up in paths_up:
            loc = path_down[2].split(" ")
            x, y = int(loc[0]), int(loc[1])
            if path_down[2] == path_up[2]:
                curr_path = path_down[0] + invert_path(path_up[0])
                curr_val = path_down[1] + path_up[1] - grid[x][y]
                if curr_val > max_val:
                    max_val = curr_val
                    max_path = curr_path

    return max_val, max_path


def invert_path(path):
    new_path = list()
    n = len(path) - 1
    for x in range(n, -1, -1):
        path_element = path[x]
        if path_element == "U":
            new_path.append("D")
        else:
            new_path.append("R")
    return new_path


def find_path_bidirectional(grid, m_processing):

    if m_processing:
        manager = multiprocessing.Manager()
        return_list = manager.list()
        p1 = Process(target=find_path_dfs_bidi_down, args=(grid, return_list))
        p1.start()
        p2 = Process(target=find_path_dfs_bidi_up, args=(grid, return_list))
        p2.start()
        p1.join()
        p2.join()
        print(return_list)
        return None, None
    else:
        # The code below negates the benefits of multiprocessing
        dummy_list = list()
        down = find_path_dfs_bidi_down(grid, dummy_list)
        up = find_path_dfs_bidi_up(grid, dummy_list)
        val, path = resolve_bidi_paths(down, up, grid)
        return val, path


def main():
    n = 3
    grid = generate_grid(n, 100)
    val, path = find_path_bidirectional(grid, False)

    print_map(grid)
    print("-----")
    print(val)
    print_path(path)


if __name__ == '__main__':
    main()