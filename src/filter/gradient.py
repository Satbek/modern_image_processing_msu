import math
from util.math.convolution import convolve1d

def _gauss_derivative(x, sigma):
    return  (-2 * x / sigma ** 2) * math.exp(-0.5 * (x**2) / sigma**2) / (math.sqrt(2 * math.pi * sigma ** 2))

def _gauss_derivative_filter(sigma):
    sigma = int(sigma + 1)
    return [_gauss_derivative(i, sigma) for i in range(-3 * sigma, 3 * sigma + 1)]

def _proccess_x(array, mode, sigma):
    kernel = _gauss_derivative_filter(sigma)
    return convolve1d(array, kernel, mode, axis = 1)

def _proccess_y(array, mode, sigma):
    kernel = _gauss_derivative_filter(sigma)
    return convolve1d(array, kernel, mode, axis = 0)

def gradient(array, mode, sigma):
    """
    Модуль градиента с помощью производной фильтра Гаусса.
    array: двумерный массив
    mode: тип экстраполяции
    sigma: радиус размытия
    result: двумерный массив
    """
    tmp1 = _proccess_x(array, mode, sigma)
    tmp2 = _proccess_y(array, mode, sigma)
    result = []
    for i in range(len(tmp1)):
        result.append([])
        for j in range(len(tmp1[0])):
            result[i].append(math.sqrt(tmp1[i][j]**2 + tmp2[i][j]**2))
    return result
