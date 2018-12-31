from collections import defaultdict

from benchmark import benchmark
from custom_io import read_lines


def lines_to_coords(lines):
    # #1 @ 509,796: 18x15
    for line in lines:
        s = line.split(' ')
        name = s[0][1:]
        base = s[2][:-1].split(',')  # remove trailing :
        size = s[3].split('x')
        x0 = int(base[0])
        y0 = int(base[1])
        x1 = int(size[0])
        y1 = int(size[1])

        for x in range(x0, x0 + x1):
            for y in range(y0, y0 + y1):
                yield name, x, y


# O(n): # of tiles with >= 2 overlaps
@benchmark
def part_1(lines):  # 121259
    result = 0
    coords = defaultdict(int)

    for coord in lines_to_coords(lines):
        c = (coord[1], coord[2], )
        coords[c] += 1

        if (coords[c]) == 2:
            result += 1

    print('part 1: %d' % result)


# O(n^2): the claim not overlapping any other
@benchmark
def part_2(lines):  # 239
    # Read coords
    seen = []
    acceptable = []
    coords = defaultdict(list)

    for coord in lines_to_coords(lines):
        name = coord[0]

        if name not in seen:
            seen.append(name)
            acceptable.append(name)

        c = (coord[1], coord[2], )
        coords[c].append(name)

        if len(coords[c]) > 1:
            for name in coords[c]:
                if name in acceptable:
                    acceptable.remove(name)

    print('part 2: %s' % acceptable)


@benchmark
def part_2_original(lines):
    # Read coords
    seen = []
    coords = defaultdict(list)

    for coord in lines_to_coords(lines):
        name = coord[0]

        if name not in seen:
            seen.append(name)

        c = (coord[1], coord[2], )
        coords[c].append(name)

    # Check what is ok and what isn't
    acceptable = seen.copy()

    for names in coords.values():
        if len(names) > 1:
            for name in names:
                if name in acceptable:
                    acceptable.remove(name)

    print('part 2: %s' % acceptable)


@benchmark
def part_2_v2(lines):
    # Read coords
    seen = []
    coords = defaultdict(list)
    map = defaultdict(list)

    for coord in lines_to_coords(lines):
        name = coord[0]

        if name not in seen:
            seen.append(name)

        c = (coord[1], coord[2], )
        coords[c].append(name)
        map[name].append(c)

    # Check what is ok and what isn't
    acceptable = seen.copy()

    for name, xcoords in map.items():
        for coord in xcoords:
            if len(coords[coord]) > 1:
                acceptable.remove(name)
                break

    print('part 2: %s' % acceptable)

@benchmark
def part_2_v3(lines):
    # Read coords
    coords = defaultdict(list)
    overlaps_per_claim = {}

    for coord in lines_to_coords(lines):
        name = coord[0]
        c = (coord[1], coord[2], )

        if name not in overlaps_per_claim.keys():
            overlaps_per_claim[name] = set()

        for n in coords[c]:
            overlaps_per_claim[name].add(n)
            overlaps_per_claim[n].add(name)
        coords[c].append(name)

    # Check what is ok and what isn't
    acceptable = [name for name, overlaps in overlaps_per_claim.items() if len(overlaps) == 0]

    print('part 2: %s' % acceptable)


# read file
lines = read_lines('data/day3.txt')

# part 1
part_1(lines)

# part 2
part_2(lines)
part_2_original(lines)
part_2_v2(lines)
part_2_v3(lines)
