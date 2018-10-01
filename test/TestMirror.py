import unittest
import sys
sys.path.append('../src')
from util.test import tolist
from transform.mirror import mirror, _mirror_x, _mirror_y
import numpy as np


class TestMirror(unittest.TestCase):
    """
    Тесты на отражение по вертикали и горизонтали
    """
    def test_mirror_x_3x3(self):
        input_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        output_arr = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
        self.assertEqual(output_arr, _mirror_x(input_arr))

    def test_mirror_y_3x3(self):
        input_arr = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]]
        output_arr = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
        self.assertEqual(output_arr, _mirror_y(input_arr))

    def test_random_mirror_x_7x7(self):
        input_arr = tolist(np.random.uniform(1,10,(7,7)))
        output_arr = tolist(np.fliplr(input_arr))
        self.assertEqual(output_arr, _mirror_x(input_arr))

    def test_random_mirror_y_7x7(self):
        input_arr = tolist(np.random.uniform(1,10,(7,7)))
        output_arr = tolist(np.flipud(input_arr))
        self.assertEqual(output_arr, _mirror_y(input_arr))

    def test_random_mirror_x_7x8(self):
        input_arr = tolist(np.random.uniform(1,10,(7,8)))
        output_arr = tolist(np.fliplr(input_arr))
        self.assertEqual(output_arr, _mirror_x(input_arr))

    def test_random_mirror_y_7x8(self):
        input_arr = tolist(np.random.uniform(1,10,(7,8)))
        output_arr = tolist(np.flipud(input_arr))
        self.assertEqual(output_arr, _mirror_y(input_arr))

    def test_empty_array(self):
        input_arr = []
        output_arr = []
        self.assertEqual(output_arr, _mirror_y(input_arr))
        self.assertEqual(output_arr, _mirror_x(input_arr))
        self.assertEqual(output_arr, mirror(input_arr, 'x'))
        self.assertEqual(output_arr, mirror(input_arr, 'y'))

    def test_mirror(self):
        input_arr = tolist(np.random.uniform(1,10,(7,7)))
        output_arr_y = tolist(np.flipud(input_arr))
        self.assertEqual(output_arr_y, mirror(input_arr, 'y'))
        output_arr_x = tolist(np.fliplr(input_arr))
        self.assertEqual(output_arr_x, mirror(input_arr, 'x'))


if __name__ == '__main__':
    unittest.main()
