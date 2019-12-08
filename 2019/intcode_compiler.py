import os
import re
import sys

from benchmark import benchmark
from custom_io import read


def is_numeric(s):
    return re.match('^-?\\d+$', s)


def lexer(code):
    tokens = []
    s = ''
    charNum = 0  # TODO correct this num
    lineNum = 1

    for c in code:
        if not c.isspace():
            s += c
            charNum += 1
            continue

        if len(s) > 0:
            tokens.append((s, charNum, lineNum))
            s = ''

        if c == '\n':
            lineNum += 1
        charNum += 1

    if len(s) > 0:
        tokens.append((s, charNum, lineNum))

    return tokens


class IntCodeCompiler:
    def __init__(self, code):
        self.code = code
        self.variables = set()
        self.allocated_variables = {}  # variable name to memory location
        self.program = []

    def parse_assign(self, variable, value, lineNum):
        """ Implemented as adding N + 0. """
        opcode = 1
        self.variables.add(variable)

        if is_numeric(variable):
            raise Exception(f'{lineNum}: You cannot assign to a literal: {variable}')

        if not is_numeric(value):
            if value not in self.variables:
                raise Exception(f'{lineNum}: You cannot access a variable before it is declared: {value}')
            parsed_value = value
        else:
            opcode += 100
            parsed_value = int(value)

        opcode += 1000  # second number is a constant

        self.program.append(opcode)
        self.program.append(parsed_value)
        self.program.append(0)
        self.program.append(variable)

    def parse_input(self, variable, lineNum):
        opcode = 3

        if is_numeric(variable):
            raise Exception(f'{lineNum}: You cannot assign a value to a literal value {variable}')

        self.variables.add(variable)
        self.program.append(opcode)
        self.program.append(variable)

    def parse_print(self, symbol, lineNum):
        opcode = 4
        argument = symbol[6:-1]

        if not is_numeric(argument):
            if argument not in self.variables:
                raise Exception(f'{lineNum}: You cannot access a variable before it is declared: {argument}')
            value = argument
            self.variables.add(argument)
        else:
            opcode += 100
            value = int(argument)

        self.program.append(opcode)
        self.program.append(value)

    def parse_math_and_assign(self, operation, variable, lhs, rhs, lineNum):
        opcode = 1 if operation == '+' else 2
        self.variables.add(variable)

        if not is_numeric(lhs):
            if lhs not in self.variables:
                raise Exception(f'{lineNum}: You cannot access a variable before it is declared: {lhs}')
            parsed_lhs = lhs
        else:
            opcode += 100
            parsed_lhs = int(lhs)

        if not is_numeric(rhs):
            if rhs not in self.variables:
                raise Exception(f'{lineNum}: You cannot access a variable before it is declared: {rhs}')
            parsed_rhs = rhs
        else:
            opcode += 1000
            parsed_rhs = int(rhs)

        self.program.append(opcode)
        self.program.append(parsed_lhs)
        self.program.append(parsed_rhs)
        self.program.append(variable)

    @benchmark
    def compile(self):
        tokens = lexer(self.code)

        for i, token in enumerate(tokens):
            symbol = token[0]
            lineNum = token[2]

            if symbol == '=':
                if i == 0:
                    raise Exception(f'{lineNum}: Unexpected =')

                if tokens[i + 1][0] == 'input()':
                    self.parse_input(tokens[i - 1][0], lineNum)
                    i += 1
                    continue
                elif i + 2 < len(tokens) and tokens[i + 2][0] in ['+', '*']:
                    self.parse_math_and_assign(tokens[i + 2][0], tokens[i - 1][0], tokens[i + 1][0], tokens[i + 3][0], lineNum)
                    i += 3
                    continue
                else:
                    self.parse_assign(tokens[i - 1][0], tokens[i + 1][0], lineNum)
                    i += 1
                    continue

            if symbol.startswith('print'):
                self.parse_print(symbol, lineNum)
                continue

        self.program.append(99)  # halt
        self.allocate_variables_pointers()
        self.update_variables_pointers()
        return self.program

    def allocate_variables_pointers(self):
        start_ptr = len(self.program)

        for variable in sorted(self.variables):  # for a consistent order, so our tests will not be fragile
            self.allocated_variables[variable] = start_ptr
            self.program.append(0)  # initialize variable memory locations to 0
            start_ptr += 1

    def update_variables_pointers(self):
        for i, val in enumerate(self.program):
            if isinstance(val, str):
                self.program[i] = self.allocated_variables[val]


if __name__ == '__main__':
    code_file = sys.argv[1]
    code = read(code_file)

    compiler = IntCodeCompiler(code)
    program = compiler.compile()

    str_program = [str(p) for p in program]
    program_file_contents = ','.join(str_program)

    output_file = os.path.splitext(code_file)[0] + '.ic'

    with open(output_file, 'w') as fh:
        fh.write(program_file_contents)
