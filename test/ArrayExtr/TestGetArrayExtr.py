import unittest
import sys
sys.path.append('../../src')
from filter.ArrayExtr.base.ArrayExtr import ArrayExtr, GetArrayExtr
from filter.ArrayExtr.ArrayOddExtr import ArrayOddExtr
from filter.ArrayExtr.ArrayConstantExtr import ArrayConstantExtr

class TestGetArrayExtr(unittest.TestCase):
    """
    Тесты получения нужного класса для экстраполяции
    """
    def test_ArrayOddExtr(self):
        obj = GetArrayExtr([1,2,3,4,5], 'odd')
        self.assertIsInstance(obj, ArrayOddExtr)

    def test_ArrayConstantExtr(self):
        obj = GetArrayExtr([1,2,3,4,5], 'constant', constant = 1)
        self.assertIsInstance(obj, ArrayConstantExtr)

    def test_unsupported_type(self):
        with self.assertRaises(ValueError) as cm:
            obj = GetArrayExtr([1,2,3,4,5], 'unsupported type')
        the_exception = cm.exception
        self.assertIsInstance(the_exception, ValueError)

if __name__ == '__main__':
    unittest.main()
