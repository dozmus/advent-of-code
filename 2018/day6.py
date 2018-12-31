from collections import defaultdict
from operator import itemgetter

from benchmark import benchmark
from custom_io import read_lines


def manhattan_distance(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


def closest(x, y, coords):
    closest_distance = -1
    closest = []

    for coord in coords:
        dist = manhattan_distance(coord, (x, y))

        if closest_distance == -1 or dist < closest_distance:
            closest_distance = dist
            closest = [coord]
        elif dist == closest_distance:
            closest.append(coord)

    return closest


@benchmark
def part_1(coords):  # 3933
    # k is how far away from the edges of the region delimited by the coordinates to check
    k = 1  # if k < min(minX, minY) - this breaks
    minX = min(coords, key=itemgetter(0))[0]
    maxX = max(coords, key=itemgetter(0))[0]
    minY = min(coords, key=itemgetter(1))[1]
    maxY = max(coords, key=itemgetter(1))[1]

    x0 = minX - k
    x1 = maxX + k
    y0 = minY - k
    y1 = maxY + k

    dx = x1 - x0 + 1
    dy = y1 - y0 + 1

    # calculate the coords each square is closest to
    distances = [[[] for y in range(dy)] for x in range(dx)]

    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            adj_x = x - x0
            adj_y = y - y0
            distances[adj_x][adj_y] = closest(x, y, coords)

    # find the coord with the most tiles close to it
    # it is invalid if one of the 'edge' coords are close to it, since it means it tends towards infinity
    coords_to_count = defaultdict(int)
    bad = set()

    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            adj_x = x - x0
            adj_y = y - y0

            value = distances[adj_x][adj_y]

            if x == x0 or x == x1 or y == y0 or y == y1:
                for v in value:
                    bad.add(v)

            if len(value) == 1:
                coords_to_count[value[0]] += 1

    for coord in coords:
        if coord in bad:
            del coords_to_count[coord]

    result = max(coords_to_count.values())
    print('part 1: %d (k=%d)' % (result, k))


@benchmark
def part_2(coords):  # 41145
    target_total = 10_000  # question parameter
    x0 = min(coords, key=itemgetter(0))[0]
    x1 = max(coords, key=itemgetter(0))[0]
    y0 = min(coords, key=itemgetter(1))[1]
    y1 = max(coords, key=itemgetter(1))[1]
    result = 0

    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            distance = 0

            for coord in coords:
                distance += manhattan_distance(coord, (x, y))

            if distance < target_total:
                result += 1

    print('part 2: %d' % result)



lines = read_lines('day6.txt')

coords = [(int(line.split(', ')[0]), int(line.split(', ')[1])) for line in lines]

# part 1
part_1(coords)

# part 2
part_2(coords)
