import math
from util.math.convolution import convolve1d

def _gauss_func1d(x, sigma):
    return math.exp(-0.5 * (x**2) / sigma**2) / (math.sqrt(2 * math.pi * sigma ** 2))

def _gauss_filter1d(sigma):
    sigma = int(sigma + 1)
    return [_gauss_func1d(i, sigma) for i in range(-3 * sigma, 3 * sigma + 1)]

def gauss(array, mode, sigma):
    """
    Фильтр Гаусса
    array: двумерный массив
    mode: тип экстраполяции
    sigma: радиус размытия
    result: двумерный массив
    """
    kernel = _gauss_filter1d(sigma)
    tmp = convolve1d(array, kernel, mode, axis = 1)
    return convolve1d(tmp, kernel, mode, axis = 0)
