import unittest
import sys
sys.path.append('../../src')
from filter.ArrayExtr.base.ArrayExtr import ArrayExtr

class TestArrayExtr(unittest.TestCase):
    """
    Тесты базового класса для экстраполяции.
    """
    def setUp(self):
        self.array = ArrayExtr([1,2,3,4,5])

    def test_create(self):
        self.assertIsInstance(self.array, ArrayExtr)

    def test_getitem_exception(self):
        with self.assertRaises(RuntimeError) as cm:
            self.array[0]
        the_exception = cm.exception
        self.assertIsInstance(the_exception, RuntimeError)

if __name__ == '__main__':
    unittest.main()
