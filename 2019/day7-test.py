import unittest
from day7 import day7a, amplification_circuit, amplification_circuit_feedback_loop, day7b


class MyTestCase(unittest.TestCase):
    def test_amplification_circuit(self):
        expected = 43210

        input = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        phase = [4, 3, 2, 1, 0]
        actual = amplification_circuit(input, phase)

        self.assertEqual(expected, actual)

    def test_day7a_ex1(self):
        expected = 43210

        input = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
        actual = day7a(input)

        self.assertEqual(expected, actual)

    def test_amplification_circuit_feedback_loop(self):
        expected = 139629729

        input = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6,
                 99, 0, 0, 5]
        phase = [9, 8, 7, 6, 5]
        actual = amplification_circuit_feedback_loop(input, phase, 0)

        self.assertEqual(expected, actual)

    def test_day7b_ex1(self):
        expected = 139629729

        input = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6,
                 99, 0, 0, 5]
        actual = day7b(input)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
