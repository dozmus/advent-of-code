from itertools import cycle

from benchmark import benchmark
from custom_io import read_lines


def line_frequency(line):
    return int(line)


@benchmark
def part_1(frequencies):  # 513
    frequency = sum(frequencies)
    print('part 1: %d' % frequency)


@benchmark
def part_2(frequencies):  # 287
    # you must use a set, and not a list. since you do lots of 'contains' and 'add' operations on the data structure
    seen = set()
    frequency = 0
    result = 0

    for f in cycle(frequencies):
        if frequency in seen:
            result = frequency
            break

        seen.add(frequency)
        frequency += f

    print('part 2: %d' % result)


@benchmark
def part_2_from_reddit(frequencies):
    from itertools import accumulate, cycle
    seen = set()
    seen.add(0)  # or '+1 -1' does not work
    print(next(f for f in accumulate(cycle(frequencies)) if f in seen or seen.add(f)))


# read file
lines = read_lines('data/day1.txt')
frequencies = [line_frequency(line) for line in lines]

# part 1
part_1(frequencies)

# part 2
part_2(frequencies)
