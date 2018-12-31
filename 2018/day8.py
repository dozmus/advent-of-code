from benchmark import benchmark
from custom_io import read_lines


class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata


def parse_node(data, start_idx=0):
    children_num = int(data[start_idx])
    metadata_num = int(data[start_idx + 1])
    start_idx += 2

    children = []

    for i in range(0, children_num):
        node, next_idx = parse_node(data, start_idx)
        children.append(node)
        start_idx = next_idx

    metadata = [int(data[start_idx + i]) for i in range(0, metadata_num)]
    start_idx += metadata_num

    return Node(children, metadata), start_idx


def sum_metadata(node):
    return sum(node.metadata) + sum(sum_metadata(child) for child in node.children)


def value(node):
    if len(node.children) == 0:
        return sum(node.metadata)
    else:
        x = 0

        for m in node.metadata:
            if 0 < m <= len(node.children):
                x += value(node.children[m - 1])

        return x


@benchmark
def part_1(data):  # 47112
    node, discard = parse_node(data)
    sum = sum_metadata(node)
    print('part 1: %d' % sum)


@benchmark
def part_2(data):  # 28237
    node, discard = parse_node(data)
    result = value(node)
    print('part 2: %d' % result)
    pass


lines = read_lines('day8.txt')
data = lines[0].split(' ')

part_1(data)
part_2(data)
