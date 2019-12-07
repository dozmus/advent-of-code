import unittest

from day6 import day6a
from day6 import day6b


class MyTestCase(unittest.TestCase):
    def test_day6a_ex1(self):
        input = ['COM)B',
                 'B)C',
                 'C)D',
                 'D)E',
                 'E)F',
                 'B)G',
                 'G)H',
                 'D)I',
                 'E)J',
                 'J)K',
                 'K)L']

        expected = 42
        actual = day6a(input)

        self.assertEqual(expected, actual)

    def test_day6b_ex1(self):
        input = ['COM)B',
                 'B)C',
                 'C)D',
                 'D)E',
                 'E)F',
                 'B)G',
                 'G)H',
                 'D)I',
                 'E)J',
                 'J)K',
                 'K)L',
                 'K)YOU',
                 'I)SAN']

        expected = 4
        actual = day6b(input)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
