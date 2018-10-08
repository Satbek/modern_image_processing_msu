import unittest
import sys
sys.path.append('../../src')
from filter.ArrayExtr.ArrayConstantExtr import ArrayConstantExtr

class TestArrayConstantExtr(unittest.TestCase):
    """
    ТестыКласс для дублирования граничных пикселей
    при экстраполяции
    """
    def setUp(self):
        self.array = ArrayConstantExtr([1,2,3,4,5,6], 0)

    def test_create(self):
        self.assertIsInstance(self.array, ArrayConstantExtr)

    def test_is_extrapolation_for(self):
        self.assertTrue(ArrayConstantExtr.is_extrapolation_for('Constant'))
        self.assertTrue(ArrayConstantExtr.is_extrapolation_for('CONSTANT'))

    def test_inner(self):
        self.assertEqual(self.array[2], 3)
        self.assertEqual(self.array[1], 2)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[5], 6)

    def test_left(self):
        self.assertEqual(self.array[-1], 0)
        self.assertEqual(self.array[-2], 0)
        self.assertEqual(self.array[-6], 0)
        self.assertEqual(self.array[-1000], 0)

    def test_right(self):
        self.assertEqual(self.array[6], 0)
        self.assertEqual(self.array[7], 0)
        self.assertEqual(self.array[8], 0)
        self.assertEqual(self.array[1000], 0)

if __name__ == '__main__':
    unittest.main()