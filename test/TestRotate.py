import unittest
import sys
sys.path.append('../src')
from transform.rotate import _rot90_cw, _rot90_ccw, rotate
import numpy as np
from util.test import tolist


class TestRotate(unittest.TestCase):
    """
        Тесты на отражение по вертикали и горизонтали
    """
    def test_rot90_cw_3x3(self):
        input_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        output_arr = [[7, 4, 1],[8, 5, 2],[9, 6, 3]]
        self.assertEqual(output_arr, _rot90_cw(input_arr))

    def test_rot90_ccw_3x3(self):
        input_arr = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
        output_arr = [[3, 6, 9],[2, 5, 8],[1, 4, 7]]
        self.assertEqual(output_arr, _rot90_ccw(input_arr))

    def test__rot90_cw_7x7(self):
        input_arr = tolist(np.random.uniform(1,10,(7,7)))
        output_arr = tolist(np.rot90(input_arr, -1))
        self.assertEqual(output_arr, _rot90_cw(input_arr))

    def test_rot90_ccw_7x7(self):
        input_arr = tolist(np.random.uniform(1,10,(7,7)))
        output_arr = tolist(np.rot90(input_arr))
        self.assertEqual(output_arr, _rot90_ccw(input_arr))

    def test_rot90_cw_7x8(self):
        input_arr = tolist(np.random.uniform(1,10,(7,8)))
        output_arr = tolist(np.rot90(input_arr, -1))
        self.assertEqual(output_arr, _rot90_cw(input_arr))

    def test_rot90_ccw_7x8(self):
        input_arr = tolist(np.random.uniform(1,10,(7,8)))
        output_arr = tolist(np.rot90(input_arr))
        self.assertEqual(output_arr, _rot90_ccw(input_arr))

    def test_rot90_positive_degree(self):
        degrees = [90, 180, 270]
        input_arr = tolist(np.random.randint(1,10,(7,8)))
        for i, num in enumerate([-1,-2,-3]):
            output_arr = tolist(np.rot90(input_arr, num))
            #degrees[i] == num * (-90)
        self.assertEqual(output_arr, rotate(input_arr, degrees[i]))

    def test_rot90_negative_degree(self):
        degrees = [-90, -180, -270]
        input_arr = tolist(np.random.randint(1,10,(7,8)))
        for i, num in enumerate([1,2,3]):
            output_arr = tolist(np.rot90(input_arr, num))
            #degrees[i] == num *(-90)
        self.assertEqual(output_arr, rotate(input_arr, degrees[i]))

    def test_empty_array(self):
        input_arr = []
        output_arr = []
        self.assertEqual(output_arr, _rot90_ccw(input_arr))
        self.assertEqual(output_arr, _rot90_cw(input_arr))


if __name__ == '__main__':
    unittest.main()
