from benchmark import benchmark
from custom_io import read_lines


@benchmark
def day6a(input):
    """ input is an array of relationships. returns sum of direct and indirect relationships """
    relationships = {l.split(')')[1]: l.split(')')[0] for l in input}  # maps object -> what its orbiting
    objects = set().union(relationships.keys()).union(relationships.values())
    number = 0

    for o in objects:
        # need to count COM only once to be consistent, but it COM appears once in input => no need for special code
        while o in relationships:
            number += 1
            o = relationships[o]

    return number


def bfs_shortest_path(graph, start, goal):
    """ source: https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/"""
    explored = []
    queue = [[start]]

    if start == goal:
        return []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    return new_path

            explored.append(node)

    return None


@benchmark
def day6b(input):
    graph = {}  # node -> [ nodes you can get to through it ]

    for line in input:
        a, b = line.split(')')

        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]

        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

    path = bfs_shortest_path(graph, 'YOU', 'SAN')
    result = len(path) - 3
    # they want # of orbital transfers, so ignore YOU and SAN in the path (-2)
    # and 1 more since we arent moving in the graph but rather transfering orbit (-1)
    return result


if __name__ == '__main__':
    lines = read_lines('data/day6.txt')
    print('day6a = ' + str(day6a(lines)))  # 160040
    print('day6b = ' + str(day6b(lines)))  # 373
