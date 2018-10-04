import unittest
import sys
sys.path.append('../src')
import numpy as np
import scipy.ndimage.filters as filters
from util.test import tolist
import util.math.convolution as conv


class TestConvolution(unittest.TestCase):
    """
    Тесты на свертку
    """
    def setUp(self):
        self.array1d = [1,2,3,4,5,6]

    def test_convolve1d_1d_rep_1(self):
        kernel_even_size = [1,2,3]
        output = tolist(filters.convolve1d(self.array1d, kernel_even_size, mode = 'nearest'))
        result = conv.convolve1d(self.array1d, kernel_even_size, mode = 'rep', axis = -1)
        self.assertEqual(output, result)

    def test_convolve1d_1d_rep_2(self):
        kernel_odd_size = [1,2,3,4]
        output = tolist(filters.convolve1d(self.array1d, kernel_odd_size, mode = 'nearest'))
        result = conv.convolve1d(self.array1d, kernel_odd_size, mode = 'rep', axis = -1)
        self.assertEqual(output, result)

    def test_convolve1d_1d_odd1(self):
        kernel_even_size = [1,2,3]
        output = tolist(filters.convolve1d(self.array1d, kernel_even_size, mode = 'reflect'))
        result = conv.convolve1d(self.array1d, kernel_even_size, mode = 'odd', axis = -1)
        self.assertEqual(output, result)

    def test_convolve1d_1d_odd2(self):
        kernel_odd_size = [1,2,3,4]
        output = tolist(filters.convolve1d(self.array1d, kernel_odd_size, mode = 'reflect'))
        result = conv.convolve1d(self.array1d, kernel_odd_size, mode = 'odd', axis = -1)
        self.assertEqual(output, result)

    def test_convolve1d_1d_even(self):
        array = [1, 2, 3, 4]
        kernel = [1, 2, 3, 4]
        output = [14, 20, 29, 37]
        result = conv.convolve1d(array, kernel, mode = 'even', axis = -1)
        self.assertEqual(output, result)

    def test_convolve1d_odd_x(self):
        array = [[1,2,3],[1,2,3],[1,2,3]]
        kernel = [1,2,3]
        output = tolist(filters.convolve1d(array, kernel, axis = 1, mode = 'reflect'))
        result = conv.convolve1d(array, kernel, mode = 'odd', axis = 1)
        self.assertEqual(output, result)

    def test_convolve1d_odd_y(self):
        array = [[1,2,3],[1,2,3],[1,2,3]]
        kernel = [1,2,3]
        output = tolist(filters.convolve1d(array, kernel, axis = 0, mode = 'reflect'))
        result = conv.convolve1d(array, kernel, mode = 'odd', axis = 0)
        self.assertEqual(output, result)

    def test_convolve1d_rep_x(self):
        array = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
        kernel = [1,2,3]
        output = tolist(filters.convolve1d(array, kernel, axis = 1, mode = 'nearest'))
        result = conv.convolve1d(array, kernel, mode = 'rep', axis = 1)
        self.assertEqual(output, result)

    def test_convolve1d_rep_y(self):
        array = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
        kernel = [1,2,3,4]
        output = tolist(filters.convolve1d(array, kernel, axis = 0, mode = 'nearest'))
        result = conv.convolve1d(array, kernel, mode = 'rep', axis = 0)
        self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()
