import itertools

from benchmark import benchmark
from custom_io import read_lines


def evaluate(memory):
    pc = 0

    while pc < len(memory):
        opcode = memory[pc]

        if opcode == 1:
            a = memory[pc + 1]
            b = memory[pc + 2]
            t = memory[pc + 3]
            memory[t] = memory[a] + memory[b]
            pc += 4
        elif opcode == 2:
            a = memory[pc + 1]
            b = memory[pc + 2]
            t = memory[pc + 3]
            memory[t] = memory[a] * memory[b]
            pc += 4
        elif opcode == 99:
            break
        else:
            raise Exception('invalid opcode')


@benchmark
def day2a(program):
    program[1] = 12
    program[2] = 2
    evaluate(program)
    return str(program[0])


@benchmark
def day2b(memory):
    target = 19690720
    r = 99  # question parameter

    for i, j in itertools.product(range(r), range(r)):
        try:
            copy = memory.copy()
            copy[1] = i
            copy[2] = j
            evaluate(copy)
            result = copy[0]

            if result == target:
                return str(100 * i + j)
        except:
            # ignored, try another round
            pass

    return 'not found'


program = [int(i) for i in read_lines('data/day2.txt')[0].split(',')]

print('day 2a = ' + day2a(program.copy()))
print('day 2b = ' + day2b(program.copy()))
