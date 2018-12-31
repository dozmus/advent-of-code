from collections import defaultdict
from itertools import product

from custom_io import read_lines


def part_1(lines):  # 7350
    no_two_digits = 0
    no_three_digits = 0

    for line in lines:
        letter_counts = defaultdict(int)
        found_two_digits = False
        found_three_digits = False

        for c in line:
            letter_counts[c] += 1

        for count in letter_counts.values():
            if count == 2 and not found_two_digits:
                no_two_digits += 1
                found_two_digits = True

            if count == 3 and not found_three_digits:
                no_three_digits += 1
                found_three_digits = True

    result = no_two_digits * no_three_digits
    print('part 1: %d' % result)


def part_2(lines):  # wmlnjevbfodamyiqpucrhsukg
    print(lines)

    for a, b in product(lines, lines):
        if a == b:
            continue

        diff = letters_difference(a, b)

        if len(diff) == 1:
            idx = diff[0][0]
            result = a[:idx] + a[idx + 1:]
            print('part 2: ' + result)
            break


def letters_difference(a, b):
    # assumes len(a)=len(b)
    diff = []

    for i in range(0, len(a)):
        if a[i] != b[i]:
            diff.append((i, a[i]))

    return diff

# read file
lines = read_lines('data/day2.txt')

# part 1
part_1(lines)

# part 2
part_2(lines)
