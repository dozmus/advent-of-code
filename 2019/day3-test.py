import unittest

from custom_io import read_lines
from day3 import day3a, day3b
from day3 import intersections


class MyTestCase(unittest.TestCase):
    def test_day3a_intersection(self):
        expected = set()
        expected.add((5, 5, 20))
        expected.add((5, 6, 22))

        wire1 = 'U5,R5,U10'
        wire2 = 'R5,U5,U1'
        actual = intersections(wire1, wire2)

        self.assertEqual(expected, actual)

    def test_day3a_minimal(self):
        expected = 159

        wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
        wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
        actual = day3a([wire1, wire2])

        self.assertEqual(expected, actual)

    def test_day3b_minimal(self):
        expected = 610

        wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
        wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
        actual = day3b([wire1, wire2])

        self.assertEqual(expected, actual)

    def test_day3a(self):
        expected = 232

        wires = read_lines('data/day3.txt')
        actual = day3a(wires)

        self.assertEqual(expected, actual)

    def test_day3b(self):
        expected = 6084

        wires = read_lines('data/day3.txt')
        actual = day3b(wires)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
