import itertools

from benchmark import benchmark
from custom_io import read_lines


def intcode_day7a(memory, phase, input):
    pc = 0
    cycle = 0
    output = None
    read_phase = False

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

            if not read_phase:
                memory[a] = phase
                read_phase = True
            else:
                memory[a] = input

            pc += 2
        elif opcode == 4:  # print
            a = memory[memory[pc + 1]] if mode_a == 0 else memory[pc + 1]
            output = a
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

    return output


def amplification_circuit(program, phase):
    res_a = intcode_day7a(program.copy(), phase[0], 0)
    res_b = intcode_day7a(program.copy(), phase[1], res_a)
    res_c = intcode_day7a(program.copy(), phase[2], res_b)
    res_d = intcode_day7a(program.copy(), phase[3], res_c)
    res_e = intcode_day7a(program.copy(), phase[4], res_d)
    return res_e


@benchmark
def day7a(input):
    max_result = None
    phases = list(range(5))

    # each phase used once
    for phase in itertools.permutations(phases):
        result = amplification_circuit(input, phase)

        if max_result is None or result > max_result:
            max_result = result

    return max_result


class IntCode_Day7b:
    def __init__(self, memory, phase):
        self.memory = memory
        self.phase = phase
        self.pc = 0
        self.cycle = 0
        self.read_phase = False
        self.halted = False

    def run(self, input):
        while self.pc < len(self.memory):
            self.cycle += 1

            full_opcode = str(self.memory[self.pc])
            opcode = self.memory[self.pc] % 100
            mode_a = int(full_opcode[-3]) if len(full_opcode) >= 3 else 0
            mode_b = int(full_opcode[-4]) if len(full_opcode) >= 4 else 0

            if opcode == 1 or opcode == 2:  # add, mul
                a = self.memory[self.memory[self.pc + 1]] if mode_a == 0 else self.memory[self.pc + 1]
                b = self.memory[self.memory[self.pc + 2]] if mode_b == 0 else self.memory[self.pc + 2]
                t = self.memory[self.pc + 3]
                self.memory[t] = a * b if opcode == 2 else a + b
                self.pc += 4
            elif opcode == 3:  # input
                a = self.memory[self.pc + 1]

                if not self.read_phase:
                    self.memory[a] = self.phase
                    self.read_phase = True
                else:
                    self.memory[a] = input

                self.pc += 2
            elif opcode == 4:  # print
                a = self.memory[self.memory[self.pc + 1]] if mode_a == 0 else self.memory[self.pc + 1]
                self.pc += 2
                return a
            elif opcode == 5:  # jump-if-true
                a = self.memory[self.memory[self.pc + 1]] if mode_a == 0 else self.memory[self.pc + 1]
                b = self.memory[self.memory[self.pc + 2]] if mode_b == 0 else self.memory[self.pc + 2]

                if a != 0:
                    self.pc = b
                else:
                    self.pc += 3
            elif opcode == 6:  # jump-if-false
                a = self.memory[self.memory[self.pc + 1]] if mode_a == 0 else self.memory[self.pc + 1]
                b = self.memory[self.memory[self.pc + 2]] if mode_b == 0 else self.memory[self.pc + 2]

                if a == 0:
                    self.pc = b
                else:
                    self.pc += 3
            elif opcode == 7:  # less than
                a = self.memory[self.memory[self.pc + 1]] if mode_a == 0 else self.memory[self.pc + 1]
                b = self.memory[self.memory[self.pc + 2]] if mode_b == 0 else self.memory[self.pc + 2]
                t = self.memory[self.pc + 3]
                value = 1 if a < b else 0
                self.memory[t] = value
                self.pc += 4
            elif opcode == 8:  # equals
                a = self.memory[self.memory[self.pc + 1]] if mode_a == 0 else self.memory[self.pc + 1]
                b = self.memory[self.memory[self.pc + 2]] if mode_b == 0 else self.memory[self.pc + 2]
                t = self.memory[self.pc + 3]
                value = 1 if a == b else 0
                self.memory[t] = value
                self.pc += 4
            elif opcode == 99:
                self.halted = True
                break
            else:
                raise Exception('invalid opcode')


def amplification_circuit_feedback_loop(program, phase, seed):
    a = IntCode_Day7b(program.copy(), phase[0])
    b = IntCode_Day7b(program.copy(), phase[1])
    c = IntCode_Day7b(program.copy(), phase[2])
    d = IntCode_Day7b(program.copy(), phase[3])
    e = IntCode_Day7b(program.copy(), phase[4])

    while not e.halted:
        res_a = a.run(seed)
        res_b = b.run(res_a)
        res_c = c.run(res_b)
        res_d = d.run(res_c)
        res_e = e.run(res_d)

        if not e.halted:
            seed = res_e  # feedback

    return seed

@benchmark
def day7b(program):
    max_result = None
    phases = list(range(5, 10))

    # each phase used once
    for phase in itertools.permutations(phases):
        result = amplification_circuit_feedback_loop(program, phase, 0)

        if max_result is None or result > max_result:
            max_result = result

    return max_result


if __name__ == '__main__':
    line = [int(i) for i in read_lines('data/day7.txt')[0].split(',')]
    print('day7a = ' + str(day7a(line)))  # 75228
    print('day7b = ' + str(day7b(line)))  # 79846026
