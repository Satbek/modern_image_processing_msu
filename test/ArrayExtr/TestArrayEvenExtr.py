import unittest
import sys
sys.path.append('../../src')
from filter.ArrayExtr.ArrayEvenExtr import ArrayEvenExtr

class TestArrayEvenExtr(unittest.TestCase):
    """
    Тесты класса для нечетной экстраполяции.
    """
    def setUp(self):
    	#-4 -3 -2 -1 0 1 | 1 2 3 4 5 | 5 6 7 8 9
        self.array = ArrayEvenExtr([1,2,3,4,5])
        self.array2d = ArrayEvenExtr([  [1,2,3],
                                        [4,5,6],
                                        [7,8,9]])

    def test_create(self):
        self.assertIsInstance(self.array, ArrayEvenExtr)

    def test_trivial_get0(self):
        self.assertEqual(self.array[0], 1)

    def test_border_left_get(self):
        self.assertEqual(self.array[0], self.array[-1])

    def test_border_right_get(self):
        self.assertEqual(self.array[len(self.array.body)], self.array[len(self.array.body) - 1])

    def test_left(self):
        self.assertEqual(self.array[-2], 0)

    def test_right(self):
        self.assertEqual(self.array[6], 6)

    def test_getitem_exception(self):
        with self.assertRaises(IndexError) as cm:
            self.array[20]
        the_exception = cm.exception
        self.assertIsInstance(the_exception, IndexError)

    def test_inner2d(self):
        self.assertEqual(self.array2d[0][0], 1)
        self.assertEqual(self.array2d[1][1], 5)

    def test_right2d(self):
        self.assertEqual(self.array2d[0][3], 3)
        self.assertEqual(self.array2d[0][4], 4)
        self.assertEqual(self.array2d[0][5], 5)
        self.assertEqual(self.array2d[1][3], 6)
        self.assertEqual(self.array2d[1][4], 7)
        self.assertEqual(self.array2d[1][5], 8)

    def test_left2d(self):
        self.assertEqual(self.array2d[0][-1], 1)
        self.assertEqual(self.array2d[0][-2], 0)
        self.assertEqual(self.array2d[0][-3], -1)
        self.assertEqual(self.array2d[1][-1], 4)
        self.assertEqual(self.array2d[1][-2], 3)
        self.assertEqual(self.array2d[1][-3], 2)

    def test_up2d(self):
        self.assertEqual(self.array2d[-1][0], 1)
        self.assertEqual(self.array2d[-1][1], 2)
        self.assertEqual(self.array2d[-1][2], 3)
        self.assertEqual(self.array2d[-2][0], -2)
        self.assertEqual(self.array2d[-2][1], -1)
        self.assertEqual(self.array2d[-2][2], 0)
        self.assertEqual(self.array2d[-2][-1], -2)
        self.assertEqual(self.array2d[-2][-2], -3)
        self.assertEqual(self.array2d[-2][-3], -4)
        self.assertEqual(self.array2d[-2][3], 0)
        self.assertEqual(self.array2d[-2][4], 1)
        self.assertEqual(self.array2d[-2][5], 2)

    def test_down2d(self):
        self.assertEqual(self.array2d[3][0], 7)
        self.assertEqual(self.array2d[3][1], 8)
        self.assertEqual(self.array2d[3][2], 9)
        self.assertEqual(self.array2d[4][0], 10)
        self.assertEqual(self.array2d[4][1], 11)
        self.assertEqual(self.array2d[4][2], 12)
        # self.assertEqual(self.array2d[4][-1], 7)
        # self.assertEqual(self.array2d[4][-2], 7)
        # self.assertEqual(self.array2d[4][-3], 7)
        # self.assertEqual(self.array2d[4][3], 9)
        # self.assertEqual(self.array2d[4][4], 9)
        # self.assertEqual(self.array2d[4][5], 9)

    def test_is_extrapolation_for(self):
        self.assertTrue(ArrayEvenExtr.is_extrapolation_for('eVen'))
        self.assertTrue(ArrayEvenExtr.is_extrapolation_for('EVEn'))

if __name__ == '__main__':
    unittest.main()