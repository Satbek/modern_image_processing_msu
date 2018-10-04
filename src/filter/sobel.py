import sys
sys.path.append('..')
from util.math.convolution import convolve1d
def sobel(array, direction, mode):
    """
    Фильтр собеля,применямый к двумерному массиву array.
    array: двумерный массив, для которого вычисляются градиенты
    mode: тип продолжения
        rep - дублирование граничных пикселей
        odd - четное продолжение
        even - нечетное продолжение
    direction:
        x - горизонтальные контуры
        y - вертикальные контуры
    result: двумерный массив
    Алгоритм реализуется применением одномерный сверток по строкам и по столбцам.
    """
    if direction == "x":
        tmp_by_rows = convolve1d(array, [1, 0, -1], mode = mode, axis = 1)
        return convolve1d(tmp_by_rows, [1, 2, 1], mode = mode, axis = 0)
    elif direction == "y":
        tmp_by_rows = convolve1d(array, [1, 2, 1], mode = mode, axis = 1)
        return convolve1d(tmp_by_rows, [1, 0, -1], mode = mode, axis = 0)
    else:
        raise ValueError("Unsupported direction : " + direction)