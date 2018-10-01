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

if __name__ == '__main__':
    unittest.main()
