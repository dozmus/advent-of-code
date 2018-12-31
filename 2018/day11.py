import itertools
from collections import defaultdict

from benchmark import benchmark
from custom_io import read_lines


def power(x, y, input):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += input
    power_level *= rack_id

    z = 0 if power_level < 100 else int((power_level % 1000) / 100)
    return z - 5


def solve(r, input):
    largest = None
    result_coords = None

    rng = [i for i in range(0, r + 1)]

    for x in range(1, 302 - len(rng)):
        for y in range(1, 302 - len(rng)):
            pwr = 0

            for e in itertools.product(rng, rng):
                pwr += power(x + e[0], y + e[1], input)

            if largest is None or pwr > largest:
                largest = pwr
                result_coords = (x, y)

    return result_coords, largest


@benchmark
def part_1(input):  # 21,61 @ 30
    sol = solve(2, input)
    result_coords = sol[0]
    largest = sol[1]

    print('part 1: %d,%d @ %d' % (result_coords[0], result_coords[1], largest))


@benchmark
def part_2(input):  # 232,251,12
    # create summed table
    sat = defaultdict(int)
    r = [i for i in range(1, 301)]

    for coord in itertools.product(r, r):
        x = coord[0]
        y = coord[1]

        sat[coord] = power(x, y, input) + sat[(x - 1, y)] + sat[(x, y - 1)] - sat[(x - 1, y - 1)]

    # apply summed area table
    # TODO impl
    result = None

    for r in range(1, 301):
        for x in range(r + 1, 301):
            for y in range(r + 1, 301):
    # for r in range(0, 301):
    #     for x in range(1, 301 - r):
    #         for y in range(1, 301 - r):
                # pwr = sat[(x + r, y + r)] - sat[(x - 1, y)] - sat[(x, y - 1)] + sat[(x - 1, y - 1)]
                pwr = sat[(x, y)] - sat[(x - r, y)] - sat[(x, y - r)] + sat[(x - r, y - r)]

                if result is None or pwr > result[0]:
                    result = (pwr, (x, y), r + 1)

    print('part 2: %d,%d,%d @ %d' % (result[1][0], result[1][1], result[2], result[0]))


input = int(read_lines('data/day11.txt')[0])

# part_1(input)
part_2(input)
