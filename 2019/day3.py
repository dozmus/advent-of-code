from benchmark import benchmark
from custom_io import read_lines


def points_in_wire(wire):
    """ returns (point_x, point_y, distance_to_point) """
    current = (0, 0, 0)

    for path in wire.split(','):
        dir = path[0]
        dist = int(path[1:])

        delx = 0
        dely = 0

        if dir == 'R':
            delx = 1
        elif dir == 'L':
            delx = -1
        elif dir == 'U':
            dely = 1
        elif dir == 'D':
            dely = -1

        for i in range(dist):
            current = (current[0] + delx, current[1] + dely, current[2] + 1)
            yield current


def intersections(wire1, wire2):
    wire1_points = {(point[0], point[1],): point for point in set(points_in_wire(wire1))}
    wire2_points = {(point[0], point[1],): point for point in set(points_in_wire(wire2))}
    results = set()

    for key in wire1_points.keys():
        if key in wire2_points.keys():
            r1 = wire1_points[key]
            r2 = wire2_points[key]
            x = (r1[0], r1[1], r1[2] + r2[2], )
            results.add(x)

    return results


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def closest_to(points):
    centre = (0, 0)
    min_point = min(points, key=lambda x: manhattan_distance(centre, x))
    return manhattan_distance(centre, min_point)


def minimum_distance(points):
    min_point = min(points, key=lambda x: x[2])
    return min_point[2]


@benchmark
def day3a(wires):
    x = intersections(wires[0], wires[1])
    closest = closest_to(x)
    return closest


@benchmark
def day3b(wires):
    x = intersections(wires[0], wires[1])
    min_dist = minimum_distance(x)
    return min_dist


wires = read_lines('data/day3.txt')

print('day3a = ' + str(day3a(wires)))  # 232
print('day3b = ' + str(day3b(wires)))  # 6084
