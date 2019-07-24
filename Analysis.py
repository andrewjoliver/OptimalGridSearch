import time
from GridSetUp import generate_grid
from RecursiveSearch import find_path_recursive
from AStarSearch import find_path_a_star


def run_time_analysis(function, n):
    times = list()
    for x in range(2, n+1):
        t0 = time.time()

        main_grid = generate_grid(n)
        function(main_grid)

        t1 = time.time()
        total = t1 - t0
        times.append((x, total))
    return times


def accuracy_analysis(num_trials, n, max_range):
    avg_error = list()

    for x in range(0, num_trials):
        main_grid = generate_grid(n, max_range)
        val, path = find_path_recursive(main_grid, 0, 0, "", main_grid[0][0])
        val1, path1 = find_path_a_star(main_grid)

        res = (val - val1) / val
        avg_error.append(res)

    return sum(avg_error) / len(avg_error)


if __name__ == '__main__':
    num_trials = 10
    n = 12
    max_range = 5
    error = accuracy_analysis(num_trials, n, max_range)
    print(error)