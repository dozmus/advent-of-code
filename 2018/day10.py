import re

from benchmark import benchmark
from custom_io import read_lines

import matplotlib.pyplot as plt


def exists_within_range(p, points, r):
    for i in range(1, r + 1):
        if (p[0], p[1] + i) in points:
            return True
        if (p[0], p[1] - i) in points:
            return True
        if (p[0] + i, p[1]) in points:
            return True
        if (p[0] - i, p[1]) in points:
            return True
        if (p[0] - i, p[1] + i) in points:
            return True
        if (p[0] + i, p[1] + i) in points:
            return True
        if (p[0] + i, p[1] - i) in points:
            return True
        if (p[0] - i, p[1] - i) in points:
            return True

    return False


# ......................
# ......................
# ......................
# ......................
# ......#...#..###......
# ......#...#...#.......
# ......#...#...#.......
# ......#####...#.......
# ......#...#...#.......
# ......#...#...#.......
# ......#...#...#.......
# ......#...#..###......
# ......................
# ......................
# ......................
# ......................
# idea: every point is adjacent to a point, if they form a letter
@benchmark
def solve(values):  # part 1: ERCXLAJL, part 2: 10813
    bounds = 25000

    for t in range(1, bounds):
        points = set()
        bad = False

        for v in values:
            v[0] += v[2]
            v[1] += v[3]
            points.add((v[0], v[1]))

        for p in points:
            if not exists_within_range(p, points, 1):
                bad = True
                break

        if bad:
            continue

        # Plot candidate solution
        # Create data
        x = [p[0] for p in points]
        y = [-p[1] for p in points]  # since in the original plot, the top-left is (0, 0)

        # Plot
        # TODO further improvement: plot line from points adjacent to each other
        plt.scatter(x, y, c=(0, 0, 0), alpha=1)
        plt.title('day 10 (t=%d)' % t)
        plt.show()


lines = read_lines('day10.txt')
values = [[int(z) for z in re.findall(r'-?\d+', x)] for x in lines]

solve(values)
