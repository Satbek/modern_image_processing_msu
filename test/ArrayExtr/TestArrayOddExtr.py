import unittest
import sys
sys.path.append('../../src')
from filter.ArrayExtr.ArrayOddExtr import ArrayOddExtr

class TestArrayOddExtr(unittest.TestCase):
    """
    Тесты класса для четной экстраполяции.
    """
    def setUp(self):
        self.array = ArrayOddExtr([1,2,3,4,5])
        self.array2d = ArrayOddExtr([[1,2,3],[4,5,6],[7,8,9]])

    def test_create(self):
        self.assertIsInstance(self.array, ArrayOddExtr)

    def test_trivial_get0(self):
        self.assertEqual(self.array[0], 1)

    def test_border_left_get(self):
        self.assertEqual(self.array[0], self.array[-1])

    def test_border_right_get(self):
        self.assertEqual(self.array[len(self.array.body)], self.array[len(self.array.body) - 1])

    def test_left(self):
        self.assertEqual(self.array[-2], self.array[1])
        self.assertEqual(self.array[-3], self.array[2])

    def test_right(self):
        self.assertEqual(self.array[6], self.array[3])


    def test_trivial2d(self):
        self.assertEqual(self.array2d[0][0], 1)

    def test_border_up2d(self):
        self.assertEqual(self.array2d[-1][0], 1)
        self.assertEqual(self.array2d[-1][1], 2)
        self.assertEqual(self.array2d[-1][2], 3)

    def test_border_down2d(self):
        self.assertEqual(self.array2d[3][0], 7)
        self.assertEqual(self.array2d[3][1], 8)
        self.assertEqual(self.array2d[3][2], 9)

    def test_left2d(self):
        self.assertEqual(self.array2d[0][-1], 1)
        self.assertEqual(self.array2d[0][-2], 2)
        self.assertEqual(self.array2d[0][-3], 3)

    def test_right2d(self):
        self.assertEqual(self.array2d[0][3], 3)
        self.assertEqual(self.array2d[0][4], 2)
        self.assertEqual(self.array2d[0][5], 1)

    def test_down2d(self):
        self.assertEqual(self.array2d[4][0], 4)
        self.assertEqual(self.array2d[4][1], 5)
        self.assertEqual(self.array2d[4][2], 6)

    def test_up2d(self):
        self.assertEqual(self.array2d[-2][0], 4)
        self.assertEqual(self.array2d[-2][1], 5)
        self.assertEqual(self.array2d[-2][2], 6)

    def test_up_left2d(self):
        self.assertEqual(self.array2d[-2][-1], 4)
        self.assertEqual(self.array2d[-2][-2], 5)
        self.assertEqual(self.array2d[-2][-3], 6)

    def test_getitem_exception(self):
        with self.assertRaises(IndexError) as cm:
            self.array[20]
        the_exception = cm.exception
        self.assertIsInstance(the_exception, IndexError)

    def test_is_extrapolation_for(self):
        self.assertTrue(ArrayOddExtr.is_extrapolation_for('OdD'))
        self.assertTrue(ArrayOddExtr.is_extrapolation_for('Odd'))

if __name__ == '__main__':
    unittest.main()