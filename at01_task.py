import unittest
from main4 import residue


class TestDivide(unittest.TestCase):
    def test_divide_success(self):
        self.assertEqual(residue(10, 2), 0)
        self.assertEqual(residue(7, 3), 1)
        self.assertEqual(residue(73, 5), 3)

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, residue, 6, 0)


if __name__ == '__main__':
    unittest.main()

