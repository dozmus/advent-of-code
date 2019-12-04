from benchmark import benchmark


def iterate_digits(x):
    result = []

    while x > 0:
        result.insert(0, x % 10)
        x = x // 10

    return result


def is_valid_password(x):
    digits = str(x)

    if len(digits) != 6:
        return False

    has_two_consecutive = False

    for i, j in zip(digits, digits[1:]):
        if i == j:
            has_two_consecutive = True

        if i > j:  # decreasing, works since ASCII numbers
            return False

    return has_two_consecutive


def has_only_n_consecutive(x, n):
    s = ''

    for e in x:
        if len(s) == 0 or s[0] == e:
            s += e
        else:
            if len(s) == n:
                return True

            s = e

    if s != '':
        return len(s) == n

    return False


def is_valid_password_adjacents_exactly_len_2(x):
    digits = str(x)

    if len(digits) != 6:
        return False

    for i, j in zip(digits, digits[1:]):
        if i > j:  # decreasing
            return False

    return has_only_n_consecutive(digits, 2)


@benchmark
def day4a(l, u):
    passwords = [x for x in range(l, u + 1) if is_valid_password(x)]
    return len(passwords)


@benchmark
def day4b(l, u):
    passwords = [x for x in range(l, u + 1) if is_valid_password_adjacents_exactly_len_2(x)]
    return len(passwords)


lower = 264793
upper = 803935
print('day4a = ' + str(day4a(lower, upper)))  # 966
print('day4b = ' + str(day4b(lower, upper)))  # 628
