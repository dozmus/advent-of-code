from benchmark import benchmark
from custom_io import read_lines


def dependency_graph(raw):
    nodes = {}

    unique = set([e for t in raw for e in t])

    for node in unique:
        nodes[node] = set()

    for d in raw:
        nodes[d[1]].add(d[0])
    return nodes


@benchmark
def part_1(raw_dependencies, print_result=True):  # ABDCJLFMNVQWHIRKTEUXOZSYPG
    # create nodes: data -> set dependencies
    nodes = dependency_graph(raw_dependencies)

    # repeatedly take whatever is solvable, if found go to next loop to maintain alphabetical bias
    solution = []
    done = set()

    while nodes:
        for data in sorted(nodes.keys()):
            deps = nodes[data]

            if deps.issubset(done):
                solution.append(data)
                done.add(data)
                del nodes[data]
                break

    if print_result:
        print('part 1: %s' % ''.join(solution))
    return solution


class Worker:
    def __init__(self):
        self.current = None
        self.due = -1


@benchmark
def part_2(raw_dependencies):  # 896
    nodes = dependency_graph(raw_dependencies)
    solution = part_1(raw_dependencies, False)
    solution_len = len(solution)
    workers = [Worker() for i in range(0, 5)]  # 0, 5
    order = []
    elapsed = 0

    while len(order) != solution_len:
        removed = []

        for i, c in enumerate(solution):
            free = [w for w in workers if w.due <= 0]
            reqs = nodes[c]
            can_start = reqs.issubset(set(order)) and sum([1 for w in workers if w.current in reqs and w.due > 0]) == 0

            if can_start and len(free) > 0:
                # print('%s @ %d' % (c, elapsed))
                removed.append(i)
                worker = free[0]
                worker.current = c
                worker.due = ord(c) - 64 + 60

        for i in reversed(removed):
            del solution[i]

        for worker in workers:
            worker.due -= 1

            if worker.due == 0:
                order.append(worker.current)

        elapsed += 1

    print('part 2: %s / %d elapsed' % (''.join(order), elapsed))


lines = read_lines('day7.txt')
dependencies = [(line[5], line[36]) for line in lines]

part_1(dependencies)
part_2(dependencies)
