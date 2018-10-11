import unittest
import sys
sys.path.append('../src')
from filter.sobel import sobel
from scipy import ndimage
from util.test import tolist

class TestSobel(unittest.TestCase):
	"""
		Тесты фильтра Собеля
	"""
	def setUp(self):
		self.array = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

	def test_sobel_x_odd(self):
		output = tolist(ndimage.sobel(self.array, axis = 1, mode = 'reflect'))
		result = sobel(self.array, direction = 'x', mode = 'odd')
		self.assertEqual(output, result)

	def test_sobel_y_odd(self):
		output = tolist(ndimage.sobel(self.array, axis = 0, mode = 'reflect'))
		result = sobel(self.array, direction = 'y', mode = 'odd')
		self.assertEqual(output, result)

	def test_sobel_x_rep(self):
		output = tolist(ndimage.sobel(self.array, axis = 1, mode = 'nearest'))
		result = sobel(self.array, direction = 'x', mode = 'rep')
		self.assertEqual(output, result)

	def test_sobel_y_rep(self):
		output = tolist(ndimage.sobel(self.array, axis = 0, mode = 'nearest'))
		result = sobel(self.array, direction = 'y', mode = 'rep')
		self.assertEqual(output, result)

	def test_sobel_x_even(self):
		output = [[4, 8, 8, 4], [4, 8, 8, 4], [4, 8, 8, 4]]
		result = sobel(self.array, direction = 'x', mode = 'even')
		self.assertEqual(output, result)

	def test_sobel_y_even(self):
		output = [[16, 16, 16, 16],[32, 32, 32, 32],[16, 16, 16, 16]]
		result = sobel(self.array, direction = 'y', mode = 'even')
		self.assertEqual(output, result)