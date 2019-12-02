import unittest

from day2 import evaluate


class MyTestCase(unittest.TestCase):
    def test_day1a_1(self):
        expected = [2, 0, 0, 0, 99]
        input = [1, 0, 0, 0, 99]
        evaluate(input)

        self.assertEqual(expected, input)

    def test_day1a_2(self):
        expected = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        input = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        evaluate(input)

        self.assertEqual(expected, input)


if __name__ == '__main__':
    unittest.main()
