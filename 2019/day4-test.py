import unittest

from day4 import is_valid_password, day4a, is_valid_password_adjacents_exactly_len_2, day4b


class MyTestCase(unittest.TestCase):
    def test_is_valid_password(self):
        self.assertFalse(is_valid_password(266000))
        self.assertTrue(is_valid_password(111111))
        self.assertTrue(is_valid_password(122345))
        self.assertFalse(is_valid_password(123456))
        self.assertFalse(is_valid_password(100000))

    def test_is_valid_password_adjacents_exactly_len_2(self):
        self.assertTrue(is_valid_password_adjacents_exactly_len_2(112233))
        self.assertFalse(is_valid_password_adjacents_exactly_len_2(123444))
        self.assertTrue(is_valid_password_adjacents_exactly_len_2(111122))

    def test_day4a(self):
        expected = 966

        lower = 264793
        upper = 803935

        actual = day4a(lower, upper)

        self.assertEqual(expected, actual)

    def test_day4b(self):
        expected = 628

        lower = 264793
        upper = 803935

        actual = day4b(lower, upper)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
