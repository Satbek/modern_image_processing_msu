import unittest
import sys
sys.path.append('../src')
from transform import normalize

class TestNormalize(unittest.TestCase):
	"""
	Тесты модуля для нормировки изображений.
	"""
	def setUp(self):
		self.array = [[1,2,3,300],[5,6,7,-200],[9,10,11,12]]

	def test_suppress_ejection(self):
		output = [[1,2,3,255],[5,6,7,0],[9,10,11,12]]
		result = normalize.suppress_ejection(self.array, 0, 255)
		self.assertEqual(output, result)

	def test_shift(self):
		output = [[2,3,4,301],[6,7,8,-199],[10,11,12,13]]
		result = normalize.shift(self.array, 1)
		self.assertEqual(output, result)
