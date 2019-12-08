import unittest

from .intcode_compiler import IntCodeCompiler


class MyTestCase(unittest.TestCase):
    def compile(self, code):
        compiler = IntCodeCompiler(code)
        return compiler.compile()

    def test_can_add_literals(self):
        expected = [1101, 1, 2, 5, 99, 0]

        code = 'x = 1 + 2'
        actual = self.compile(code)

        self.assertEqual(expected, actual)

    def test_can_multiply_literals(self):
        expected = [1102, 1, 2, 5, 99, 0]

        code = 'x = 1 * 2'
        actual = self.compile(code)

        self.assertEqual(expected, actual)

    def test_can_handle_add_literal_negative(self):
        expected = [1101, 0, 0, 11, 1101, -1, 0, 12, 4, 12, 99, 0, 0]

        code = '''x = 0
                  y = -1
                  print(y)'''
        actual = self.compile(code)

        self.assertEqual(expected, actual)

    def test_can_assign_literal(self):
        expected = [1101, 5, 0, 5, 99, 0]

        code = 'x = 5'
        actual = self.compile(code)

        self.assertEqual(expected, actual)

    def test_can_assign_negative_literal(self):
        expected = [1101, -5, 0, 5, 99, 0]

        code = 'x = -5'
        actual = self.compile(code)

        self.assertEqual(expected, actual)

    def test_cant_assign_to_literal(self):
        code = '5 = 5'
        self.assertRaises(Exception, self.compile, code)

    def test_cant_assign_from_non_existent_variable(self):
        code = 'x = z'
        self.assertRaises(Exception, self.compile, code)

    def test_can_assign_from_variable(self):
        expected = [1101, 5, 0, 9, 1001, 9, 0, 10, 99, 0, 0]

        code = '''x = 5
                  z = x'''
        actual = self.compile(code)

        self.assertEqual(expected, actual)

    def test_print_literal(self):
        expected = [104, 1, 99]

        code = '''print(1)'''
        actual = self.compile(code)

        self.assertEqual(expected, actual)

    def test_assign_from_input(self):
        expected = [3, 3, 99, 0]

        code = '''x = input()'''
        actual = self.compile(code)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
