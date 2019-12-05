from benchmark import benchmark
from custom_io import read_lines


@benchmark
def day5a(memory):
    pc = 0
    cycle = 0

    while pc < len(memory):
        cycle += 1

        full_opcode = str(memory[pc])
        opcode = memory[pc] % 100
        mode_a = int(full_opcode[-3]) if len(full_opcode) >= 3 else 0
        mode_b = int(full_opcode[-4]) if len(full_opcode) >= 4 else 0

        if opcode == 1 or opcode == 2:
            a = memory[memory[pc + 1]] if mode_a == 0 else memory[pc + 1]
            b = memory[memory[pc + 2]] if mode_b == 0 else memory[pc + 2]
            t = memory[pc + 3]
            memory[t] = a * b if opcode == 2 else a + b
            pc += 4
        elif opcode == 3:
            a = memory[pc + 1]
            value = input('> ')
            memory[a] = int(value)
            pc += 2
        elif opcode == 4:
            a = memory[memory[pc + 1]] if mode_a == 0 else memory[pc + 1]
            print(a)
            pc += 2
        elif opcode == 99:
            break
        else:
            raise Exception('invalid opcode')


@benchmark
def day5b(memory):
    pc = 0
    cycle = 0

    while pc < len(memory):
        cycle += 1

        full_opcode = str(memory[pc])
        opcode = memory[pc] % 100
        mode_a = int(full_opcode[-3]) if len(full_opcode) >= 3 else 0
        mode_b = int(full_opcode[-4]) if len(full_opcode) >= 4 else 0

        if opcode == 1 or opcode == 2:  # add, mul
            a = memory[memory[pc + 1]] if mode_a == 0 else memory[pc + 1]
            b = memory[memory[pc + 2]] if mode_b == 0 else memory[pc + 2]
            t = memory[pc + 3]
            memory[t] = a * b if opcode == 2 else a + b
            pc += 4
        elif opcode == 3:  # input
            a = memory[pc + 1]
            value = input('> ')
            memory[a] = int(value)
            pc += 2
        elif opcode == 4:  # print
            a = memory[memory[pc + 1]] if mode_a == 0 else memory[pc + 1]
            print(a)
            pc += 2
        elif opcode == 5:  # jump-if-true
            a = memory[memory[pc + 1]] if mode_a == 0 else memory[pc + 1]
            b = memory[memory[pc + 2]] if mode_b == 0 else memory[pc + 2]

            if a != 0:
                pc = b
            else:
                pc += 3
        elif opcode == 6:  # jump-if-false
            a = memory[memory[pc + 1]] if mode_a == 0 else memory[pc + 1]
            b = memory[memory[pc + 2]] if mode_b == 0 else memory[pc + 2]

            if a == 0:
                pc = b
            else:
                pc += 3
        elif opcode == 7:  # less than
            a = memory[memory[pc + 1]] if mode_a == 0 else memory[pc + 1]
            b = memory[memory[pc + 2]] if mode_b == 0 else memory[pc + 2]
            t = memory[pc + 3]
            value = 1 if a < b else 0
            memory[t] = value
            pc += 4
        elif opcode == 8:  # equals
            a = memory[memory[pc + 1]] if mode_a == 0 else memory[pc + 1]
            b = memory[memory[pc + 2]] if mode_b == 0 else memory[pc + 2]
            t = memory[pc + 3]
            value = 1 if a == b else 0
            memory[t] = value
            pc += 4
        elif opcode == 99:
            break
        else:
            raise Exception('invalid opcode')


if __name__ == '__main__':
    program = [int(i) for i in read_lines('data/day5.txt')[0].split(',')]

    day5a(program.copy())  # Input = 1, Output = 13346482
    day5b(program.copy())  # Input = 5, Output = 12111395
