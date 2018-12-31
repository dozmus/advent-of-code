from collections import defaultdict

from benchmark import benchmark
from custom_io import read_lines


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return '%d <--> %d <--> %d' % (self.prev.value, self.value, self.next.value)


@benchmark
def solve(players, last_marble):
    points = defaultdict(int)

    # begin from player 1, to hardcode initial state of list
    marble = Node(0)
    marble.prev = marble
    marble.next = marble

    for i in range(1, last_marble + 1):
        if i != 0 and i % 23 == 0:
            for x in range(0, 7):
                marble = marble.prev

            curr_player = i % players
            points[curr_player] += i
            points[curr_player] += marble.value

            marble.prev.next = marble.next
            marble.next.prev = marble.prev
            marble = marble.next
            continue
        else:
            marble = marble.next

            tmp = Node(i, marble, marble.next)
            marble.next.prev = tmp
            marble.next = tmp

            marble = tmp

    print(points)
    return max(points.values())


line = read_lines('day9.txt')[0].split(' ')
player_num = int(line[0])
last_marble_pts = int(line[6])

print('part 1: %d' % solve(player_num, last_marble_pts))  # 429943
print('part 2: %d' % solve(player_num, last_marble_pts * 100))  # 3615691746
