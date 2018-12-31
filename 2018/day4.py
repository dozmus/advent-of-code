import datetime
import functools
import operator
import re
from collections import defaultdict

from benchmark import benchmark
from custom_io import read_lines


def to_date(x):
    # [1518-07-07 00:30] wakes up
    tmp = x.split(' ')
    x = tmp[0][1:] + ' ' + tmp[1][:-1]
    return datetime.datetime.strptime(x, '%Y-%m-%d %H:%M')


def compare(x, y):
    delta = to_date(x) - to_date(y)
    return delta.total_seconds()


def time_range(x, y):
    z = x
    c = True

    while c:
        yield '%02d:%02d' % (z[0], z[1])

        z = (z[0], z[1] + 1)

        if z[1] == 60:
            z = (z[0] + 1, 0)

        if z[0] == 24 and z[1] == 0:
            z = (0, 0)

        if z == y or z == (1, 0):
            c = False


def process(lines):  # 11367
    sorted_lines = sorted(lines, key=functools.cmp_to_key(compare))
    times = {}

    for line in sorted_lines:
        # print(line)
        k = re.search(r'#\d+', line)

        l = re.search(r'\d{2}:\d{2}', line)
        l = l.group().split(':')
        l = int(l[0]), int(l[1])

        if k:
            guard_num = int(k.group()[1:])

            if guard_num not in times:
                times[guard_num] = defaultdict(int)

        elif ' w' in line:  # ' wakes up'
            awake = l

            # print('Guard #%s: %s -> %s' % (guard_num, awake, sleep))

            for time in time_range(sleep, awake):
                times[guard_num][time] += 1
        elif ' f' in line:  # ' falls asleep'
            sleep = l

    return times


# find the guard with max(total_mins_slept), then multiply its ID by the minute it slept most on
@benchmark
def part_1(lines):
    data = process(lines)
    minute_most_slept_on = -1
    max_slept_mins = -1
    max_slept_guard = -1

    for guard, times in data.items():
        slept_mins = sum(times.values())

        if len(times.items()) == 0:
            continue
        max_slept_on_min = max(times.items(), key=operator.itemgetter(1))[0]

        if slept_mins > max_slept_mins:
            minute_most_slept_on = int(max_slept_on_min.split(':')[1])
            max_slept_mins = slept_mins
            max_slept_guard = guard

    result = max_slept_guard * minute_most_slept_on
    print('Most slept guard: %s @ %s mins most slept on %d' % (max_slept_guard, max_slept_mins, minute_most_slept_on))
    print('Part 2: %d' % result)


# find the guard where for a given minute it has slept more than any other guard on any other time, then mul time by ID
@benchmark
def part_2(lines):  # 36896
    data = process(lines)
    mins_to_guards = defaultdict(list)

    for guard, times in data.items():
        for time, n in times.items():
            mins_to_guards[time].append((guard, n))

    max_guard = ''
    max_times = -1
    max_time = ''

    for time, value in mins_to_guards.items():
        for guard, times in value:
            if times > max_times:
                max_guard = guard
                max_times = times
                max_time = time

    result = max_guard * int(max_time.split(':')[1])
    print('Most slept time for a guard: %s @ %s at %d times' % (max_guard, max_time, max_times))
    print('Part 2: %d' % result)


lines = read_lines('day4.txt')

# part 1
part_1(lines)

# part 2
part_2(lines)
