import unittest
import sys
sys.path.append('../src')
from filter.median import median
from scipy.signal import medfilt
from util.test import tolist

class TestMedian(unittest.TestCase):
    """
    Тесты для медианного фильтра
    """
    def setUp(self):
        self.array = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    def test_rad1(self):
        result = median(self.array, rad = 1)
        output = tolist(medfilt(self.array, kernel_size = 3))
        self.assertEqual(output, result)

    def test_rad2(self):
        result = median(self.array, rad = 2)
        output = tolist(medfilt(self.array, kernel_size = 5))
        self.assertEqual(output, result)

    def test_rad0(self):
        result = median(self.array, rad = 0)
        output = tolist(medfilt(self.array, kernel_size = 1))
        self.assertEqual(output, result)

    def test_rad3(self):
        result = median(self.array, rad = 3)
        output = tolist(medfilt(self.array, kernel_size = 7))
        self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()