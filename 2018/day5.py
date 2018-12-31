from string import ascii_lowercase

from benchmark import benchmark
from custom_io import read_lines


def reduce(line):
    i = 0

    while i < len(line):
        if i + 1 < len(line):
            c = line[i]
            n = line[i + 1]

            if c.lower() == n.lower() and c != n:
                line = line[:i] + line[i+2:]
                i -= 1
                pass
            else:
                i += 1
        else:
            # new_line += line[i]
            i += 1

    return line


# reduce the line, where Aa => {}, aA => {}, and repetitively: e.g. ABbb => {}
@benchmark
def part_1(line):  # 10762
    chain = reduce(line)
    print('part 1: (len=%d) %s ' % (len(chain), chain))


# length of the shortest str you can produce by removing all instances of ONE letter and fully reacting the result?
# <=> take part_1, remove all of each letter and take shortest
@benchmark
def part_2(line):  # 6946
    chain = reduce(line)
    lengths = {}

    for c in ascii_lowercase:
        subchain = reduce(chain.replace(c, '').replace(c.upper(), ''))
        lengths[c] = len(subchain)

    letter = min(lengths, key=lengths.get)
    length = lengths[letter]
    print('part 2: (len=%d) %s ' % (length, letter))


line = read_lines('day5.txt')[0]

# part 1
part_1(line)

# part 2
part_2(line)
