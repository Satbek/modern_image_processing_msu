import unittest
import sys
sys.path.append('../../src')
from filter.ArrayExtr.base.ArrayExtr import ArrayExtr, GetArrayExtr
from filter.ArrayExtr.ArrayOddExtr import ArrayOddExtr

class TestArray2DExtr(unittest.TestCase):
    """
    Тесты двумерного массива с эстраполяцией.
    """
    def setUp(self):
        array = [[1,2,3],[4,5,6],[7,8,9]]
        self.array = GetArrayExtr(array, 'odd')

    def test_creation(self):
        self.assertIsInstance(self.array, ArrayOddExtr)
    
    def test_trivial(self):
        self.assertEqual(self.array[0][0], 1)

    def test_border_up(self):
        self.assertEqual(self.array[-1][0], 1)
        self.assertEqual(self.array[-1][1], 2)
        self.assertEqual(self.array[-1][2], 3)

    def test_border_down(self):
        self.assertEqual(self.array[3][0], 7)
        self.assertEqual(self.array[3][1], 8)
        self.assertEqual(self.array[3][2], 9)

    def test_left(self):
        self.assertEqual(self.array[0][-1], 1)
        self.assertEqual(self.array[0][-2], 2)
        self.assertEqual(self.array[0][-3], 3)

    def test_right(self):
        self.assertEqual(self.array[0][3], 3)
        self.assertEqual(self.array[0][4], 2)
        self.assertEqual(self.array[0][5], 1)

    def test_down(self):
        self.assertEqual(self.array[4][0], 4)
        self.assertEqual(self.array[4][1], 5)
        self.assertEqual(self.array[4][2], 6)

    def test_up(self):
        self.assertEqual(self.array[-2][0], 4)
        self.assertEqual(self.array[-2][1], 5)
        self.assertEqual(self.array[-2][2], 6)

    def test_up_left(self):
        self.assertEqual(self.array[-2][-1], 4)
        self.assertEqual(self.array[-2][-2], 5)
        self.assertEqual(self.array[-2][-3], 6)

if __name__ == '__main__':
    unittest.main()
