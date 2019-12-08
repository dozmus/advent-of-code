import os
import re
import sys

from benchmark import benchmark
from custom_io import read_lines


def is_str_an_int(s):
    return re.match('^-?\\d+$', s)


class IntCodeCompiler:
    def __init__(self, code):
        self.lines = code
        self.variables = set()
        self.allocated_variables = {}  # variable name to memory location

    @benchmark
    def compile(self):
        program = []

        for lineNo, line in enumerate(self.lines):
            line = line.strip()

            if '+' in line or '*' in line:
                opcode = 1 if '+' in line else 2
                lex = line.split(' ')

                variable = lex[0]
                self.variables.add(variable)

                l = lex[2]
                r = lex[4]

                if not is_str_an_int(l):
                    if l not in self.variables:
                        raise Exception(f'{lineNo}: You cannot access a variable before it is declared: {l}')
                    l_val = l
                else:
                    opcode += 100
                    l_val = int(l)

                if not is_str_an_int(r):
                    if r not in self.variables:
                        raise Exception(f'{lineNo}: You cannot access a variable before it is declared: {r}')
                    r_val = r
                else:
                    opcode += 1000
                    r_val = int(r)

                program.append(opcode)
                program.append(l_val)
                program.append(r_val)
                program.append(variable)
                continue

            if line.startswith('print'):
                opcode = 4
                argument = line[6:-1]

                if not is_str_an_int(argument):
                    if argument not in self.variables:
                        raise Exception(f'{lineNo}: You cannot access a variable before it is declared: {variable}')
                    value = argument
                    self.variables.add(argument)
                else:
                    opcode += 100
                    value = int(argument)

                program.append(opcode)
                program.append(value)
                continue

            if line.endswith(' = input()'):
                opcode = 3
                variable = line.split('=')[0].strip()

                if is_str_an_int(variable):
                    raise Exception(f'{lineNo}: You cannot assign a value to a literal value {variable}')

                self.variables.add(variable)
                program.append(opcode)
                program.append(variable)
                continue

            if '=' in line:  # assignment
                opcode = 1
                lex = line.split(' ')

                variable = lex[0].strip()
                self.variables.add(variable)

                if is_str_an_int(variable):
                    raise Exception(f'{lineNo}: You cannot assign to a literal: {variable}')

                src = lex[2].strip()

                if not is_str_an_int(src):
                    if src not in self.variables:
                        raise Exception(f'{lineNo}: You cannot access a variable before it is declared: {src}')
                    src_val = src
                else:
                    opcode += 100
                    src_val = int(src)

                opcode += 1000  # second number is a constant

                program.append(opcode)
                program.append(src_val)
                program.append(0)
                program.append(variable)
                continue

        program.append(99)
        self.allocate_variables_pointers(program)
        self.update_variables_pointers(program)
        return program

    def allocate_variables_pointers(self, program):
        start_ptr = len(program)

        for variable in sorted(self.variables):  # for a consistent order, so our tests will not be fragile
            self.allocated_variables[variable] = start_ptr
            program.append(0)  # initialize variable memory locations to 0
            start_ptr += 1

    def update_variables_pointers(self, program):
        for i, val in enumerate(program):
            if isinstance(val, str):
                program[i] = self.allocated_variables[val]


if __name__ == '__main__':
    code_file = sys.argv[1]
    code = read_lines(code_file)

    compiler = IntCodeCompiler(code)
    program = compiler.compile()

    str_program = [str(p) for p in program]
    program_file_contents = ','.join(str_program)

    output_file = os.path.splitext(code_file)[0] + '.ic'

    with open(output_file, 'w') as fh:
        fh.write(program_file_contents)
