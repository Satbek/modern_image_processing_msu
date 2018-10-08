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