from collections import defaultdict

from benchmark import benchmark
from custom_io import read_lines


def clockwise(j, length, units_clockwise):
    m = 1 if length == 0 else length
    j = (j + units_clockwise) % m

    if j == 0:  # aka next element should go on the end, due to %
        j = m
    return j


@benchmark
def solve(players, last_marble):
    marbles = []
    curr_player = 0
    points = defaultdict(int)
    j = 0

    for i in range(0, last_marble + 1):
        if i != 0 and i % 23 == 0:
            # print('[i=%d, j=%d, a(j)=%d] %s' % (i, j, marbles[j], marbles))
            j = clockwise(j, len(marbles), -7)
            y = marbles[j]
            points[curr_player] += i
            points[curr_player] += y

            # print('player[%d] += %d + %d' % (curr_player, i, y))
            del marbles[j]
            # print('[i=%d, j=%d, a(j)=%d] %s' % (i, j, marbles[j], marbles))
        else:
            j = clockwise(j, len(marbles), 2)

            marbles.insert(j, i)
            # print('[i=%d, j=%d] %s' % (i, j, marbles))

        curr_player = (curr_player + 1) % players

    return max(points.values())


line = read_lines('data/day9.txt')[0].split(' ')
player_num = int(line[0])
last_marble_pts = int(line[6])

print('part 1: %d' % solve(player_num, last_marble_pts))  # 429943
print('part 2: %d' % solve(player_num, last_marble_pts * 100))  # too slow...
