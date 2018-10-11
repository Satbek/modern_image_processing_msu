from filter.ArrayExtr.base.ArrayExtr import GetArrayExtr
from filter.ArrayExtr.ArrayConstantExtr import ArrayConstantExtr

def median(array, rad):
    """
    Медианная фильтрация, параметр rad — целочисленный радиус фильтра,
    то есть размер фильтра — квадрат со стороной (2 * rad + 1)
    array: двумерный массив
    rad: число
    result: двумерный массив
    """
    array = GetArrayExtr(array,'constant', 0)
    row_len, col_len, median_arr_len = len(array), len(array[0]), (2 * rad + 1) * (2 * rad + 1)
    result = []
    for i in range(row_len):
        result.append([])
        for j in range(col_len):
            median_arr = []
            for l in range(i - rad, i + rad + 1):
                for m in range(j - rad, j + rad + 1):
                    median_arr.append(array[l][m])
            #print("median arr[{}],[{}]".format(i,j),median_arr)
            result[i].append(sorted(median_arr)[median_arr_len // 2])
    return result
