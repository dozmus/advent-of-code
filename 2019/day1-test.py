import unittest

from day1 import fuel_required_fuel_also_requires_fuel


class Day1b(unittest.TestCase):
    def test_simple_case(self):
        mass = 14
        expected = 2
        actual = fuel_required_fuel_also_requires_fuel(mass)
        self.assertEqual(expected, actual)

    def test_recursive(self):
        mass = 1969
        expected = 966
        actual = fuel_required_fuel_also_requires_fuel(mass)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
