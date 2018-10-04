from filter.ArrayExtr.base.ArrayExtr import GetArrayExtr
#toDo убрать это, должно быть подгружено уже
from filter.ArrayExtr.ArrayOddExtr import ArrayOddExtr
from filter.ArrayExtr.ArrayEvenExtr import ArrayEvenExtr
from filter.ArrayExtr.ArrayRepExtr import ArrayRepExtr

def _convolve1d(array, kernel, mode):
    """
    Одомерная свертка одномерного массива одномерным ядром
    array: одномерный массив
    kernel: одномерный массив
    mode: тип продолжения
        rep - дублирование граничных пикселей
        odd - четное продолжение
        even - нечетное продолжение
    result: двумерный массив
    """
    array = GetArrayExtr(array, mode)
    res = []
    length_k = len(kernel)
    central_shift = (length_k - 1) // 2
    for i in range(len(array)):
        res_elem = 0
        for l, r in zip(range(length_k), reversed(range(length_k))):
            res_elem += array[i - central_shift + l] * kernel[r]
        res.append(res_elem)
    return res

def convolve1d(array, kernel, mode, axis):
    """
    Одномерная линейная свертка двумерного массива одномерным ядром.
    array: дмумерный массив или одномерный массив
    kernel: одномерный массив
    axis: 0 - по столбцам, 1 - по строкам, -1 - одномерный случай
    mode: тип продолжения
        rep - дублирование граничных пикселей
        odd - четное продолжение
        even - нечетное продолжение 
    result: двумерный массив
    """
    result = []
    if axis == 0:
        for i in range(len(array[0])):
            column = [array[j][i] for j in range(len(array))]
            result.append(_convolve1d(column, kernel, mode))
        #we need list of list
        result = [list(row) for row in zip(*result)]
    elif axis == 1:
        for row in array:
            result.append(_convolve1d(row, kernel, mode))
    elif axis == -1:
        return _convolve1d(array, kernel, mode)
    else:
        raise RuntimeError("Unsupported axis: " + str(axis))
    return result

def convolve2d(array, kernel, mode, axis):
    """
    Двумерная линейная свертка.
    array: дмумерный массив
    kernel: двумерный массив
    axis: 0 - по столбцам, 1 - по строкам
    mode: тип продолжения
        rep - дублирование граничных пикселей
        odd - четное продолжение
        even - нечетное продолжение 
    """
    return None