import unittest
import sys
sys.path.append('../../src')
from filter.ArrayExtr.ArrayRepExtr import ArrayRepExtr

class TestArrayRepExtr(unittest.TestCase):
    """
    ТестыКласс для дублирования граничных пикселей
    при экстраполяции
    """
    def setUp(self):
        self.array = ArrayRepExtr([1,2,3,4,5,6])
        self.array2d = ArrayRepExtr([[1,2,3],[4,5,6],[7,8,9]])

    def test_create(self):
        self.assertIsInstance(self.array, ArrayRepExtr)

    def test_trivial_get0(self):
        self.assertEqual(self.array[0], 1)

    def test_border_left_get(self):
        self.assertEqual(self.array[0], self.array[-1])

    def test_border_right_get(self):
        self.assertEqual(self.array[len(self.array)], self.array[len(self.array) - 1])

    def test_left(self):
        self.assertEqual(self.array[-2], self.array[0])

    def test_right(self):
        self.assertEqual(self.array[60], self.array.body[-1])

    def test_right2(self):
        self.assertEqual(self.array[len(self.array)], self.array[len(self.array) + 1])

    def test_right3(self):
        self.assertEqual(self.array[6], self.array.body[-1])

    def test_inner(self):
        for i in range(len(self.array)):
            self.assertEqual(self.array[i], self.array.body[i])

    def test_inner_right(self):
        for i in range(len(self.array), 10 * len(self.array)):
            self.assertEqual(self.array[i], self.array.body[-1])

    def test_inner2d(self):
        self.assertEqual(self.array2d[0][0], 1)
        self.assertEqual(self.array2d[1][1], 5)

    def test_right2d(self):
        self.assertEqual(self.array2d[0][3], 3)
        self.assertEqual(self.array2d[0][4], 3)
        self.assertEqual(self.array2d[0][5], 3)
        self.assertEqual(self.array2d[1][3], 6)
        self.assertEqual(self.array2d[1][4], 6)
        self.assertEqual(self.array2d[1][5], 6)

    def test_left2d(self):
        self.assertEqual(self.array2d[0][-1], 1)
        self.assertEqual(self.array2d[0][-2], 1)
        self.assertEqual(self.array2d[0][-3], 1)
        self.assertEqual(self.array2d[1][-1], 4)
        self.assertEqual(self.array2d[1][-2], 4)
        self.assertEqual(self.array2d[1][-3], 4)

    def test_up2d(self):
        self.assertEqual(self.array2d[-1][0], 1)
        self.assertEqual(self.array2d[-1][1], 2)
        self.assertEqual(self.array2d[-1][2], 3)
        self.assertEqual(self.array2d[-2][0], 1)
        self.assertEqual(self.array2d[-2][1], 2)
        self.assertEqual(self.array2d[-2][2], 3)
        self.assertEqual(self.array2d[-2][-1], 1)
        self.assertEqual(self.array2d[-2][-2], 1)
        self.assertEqual(self.array2d[-2][-3], 1)
        self.assertEqual(self.array2d[-2][4], 3)
        self.assertEqual(self.array2d[-2][5], 3)
        self.assertEqual(self.array2d[-2][6], 3)

    def test_down2d(self):
        self.assertEqual(self.array2d[3][0], 7)
        self.assertEqual(self.array2d[3][1], 8)
        self.assertEqual(self.array2d[3][2], 9)
        self.assertEqual(self.array2d[4][0], 7)
        self.assertEqual(self.array2d[4][1], 8)
        self.assertEqual(self.array2d[4][2], 9)
        self.assertEqual(self.array2d[4][-1], 7)
        self.assertEqual(self.array2d[4][-2], 7)
        self.assertEqual(self.array2d[4][-3], 7)
        self.assertEqual(self.array2d[4][3], 9)
        self.assertEqual(self.array2d[4][4], 9)
        self.assertEqual(self.array2d[4][5], 9)

    def test_is_extrapolation_for(self):
        self.assertTrue(ArrayRepExtr.is_extrapolation_for('Rep'))
        self.assertTrue(ArrayRepExtr.is_extrapolation_for('reP'))

if __name__ == '__main__':
    unittest.main()