import os
import sys

from benchmark import benchmark
from custom_io import read_lines


class IntCodeCompiler:
    def __init__(self, code):
        self.lines = code
        self.variables = {}
        self.allocated_variables = {}
        self.variable_ptr = -1

    @benchmark
    def compile(self):
        program = []

        for lineNo, line in enumerate(self.lines):
            line = line.strip()

            if '+' in line or '*' in line:
                opcode = 1 if '+' in line else 2
                lex = line.split(' ')

                variable = lex[0]
                var_ptr = self.get_or_create_variable_pointer(variable)

                l = lex[2]
                r = lex[4]

                if not l.isnumeric():
                    if l not in self.variables:
                        raise Exception(f'{lineNo}: You cannot access a variable before it is declared: {l}')
                    l_val = self.variables[l]
                else:
                    opcode += 100
                    l_val = int(l)

                if not r.isnumeric():
                    if r not in self.variables:
                        raise Exception(f'{lineNo}: You cannot access a variable before it is declared: {r}')
                    r_val = self.variables[r]
                else:
                    opcode += 1000
                    r_val = int(r)

                program.append(opcode)
                program.append(l_val)
                program.append(r_val)
                program.append(var_ptr)
                continue

            if line.startswith('print'):
                opcode = 4
                variable = line[6:-1]

                if not variable.isnumeric():
                    if variable not in self.variables:
                        raise Exception(f'{lineNo}: You cannot access a variable before it is declared: {variable}')
                    value = self.variables[variable]
                else:
                    opcode += 100
                    value = int(variable)

                program.append(opcode)
                program.append(value)
                continue

            if line.endswith(' = input()'):
                opcode = 3
                variable = line.split('=')[0].strip()

                if not variable.isnumeric():
                    value = self.get_or_create_variable_pointer(variable)
                else:
                    raise Exception(f'{lineNo}: You cannot assign a value to a literal value {variable}')

                program.append(opcode)
                program.append(value)
                continue

            if '=' in line:  # assignment
                opcode = 1
                lex = line.split(' ')

                variable = lex[0].strip()

                if variable.isnumeric():
                    raise Exception(f'{lineNo}: You cannot assign to a literal: {variable}')

                var_ptr = self.get_or_create_variable_pointer(variable)

                src = lex[2].strip()

                if not src.isnumeric():
                    if src not in self.variables:
                        raise Exception(f'{lineNo}: You cannot access a variable before it is declared: {src}')
                    src_val = self.variables[src]
                else:
                    opcode += 100
                    src_val = int(src)

                opcode += 1000  # second number is a constant

                program.append(opcode)
                program.append(src_val)
                program.append(0)
                program.append(var_ptr)
                continue

        program.append(99)
        self.allocate_variables_pointers(program)
        self.update_variables_pointers(program)
        return program

    def get_or_create_variable_pointer(self, variable):
        if variable in self.variables:
            return self.variables[variable]
        else:
            var_ptr = self.variable_ptr
            self.variables[variable] = var_ptr
            self.variable_ptr -= 1
            return var_ptr

    def allocate_variables_pointers(self, program):
        start_ptr = len(program)

        for variable in self.variables:
            self.allocated_variables[variable] = start_ptr
            program.append(0)  # initialize the variables to initial value 0
            start_ptr += 1

    def update_variables_pointers(self, program):
        for i, value in enumerate(program):
            if value < 0:
                variable = [k for k, v in self.variables.items() if v == value][0]
                allocated_ptr = self.allocated_variables[variable]
                program[i] = allocated_ptr


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

