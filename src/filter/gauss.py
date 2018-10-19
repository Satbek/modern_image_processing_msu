import math
from util.math.convolution import convolve1d

def gauss_func1d(x, sigma):
    return math.exp(-0.5 * (x**2) / sigma**2) / (math.sqrt(2 * math.pi * sigma ** 2))

def gauss_filter1d(sigma):
    sd = int(sigma + 1)
    result = [gauss_func1d(i, sigma) for i in range(-3 * sd, 3 * sd + 1)]
    return result

def gauss(array, mode, sigma):
    """
    Фильтр Гаусса
    array: двумерный массив
    mode: тип экстраполяции
    sigma: радиус размытия
    result: двумерный массив
    """
    kernel = gauss_filter1d(sigma)
    tmp = convolve1d(array, kernel, mode, axis = 1)
    result = convolve1d(tmp, kernel, mode, axis = 0)
    return result
