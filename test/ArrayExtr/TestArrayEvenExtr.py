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

    def test_is_extrapolation_for(self):
        self.assertTrue(ArrayEvenExtr.is_extrapolation_for('eVen'))
        self.assertTrue(ArrayEvenExtr.is_extrapolation_for('EVEn'))

if __name__ == '__main__':
    unittest.main()