"""
Модуль для нормировки избражений.
"""


def suppress_ejection(array, min_value = 0, max_value = 255):
    """
    Приведение значений меньших min_value к min_value,
    больших max_value к max_value.
    array: двумерный массив
    min_value: нижний порог
    max_valur: верхний порог
    result: двумерный массив
    """
    result = []
    for i in range(len(array)):
        result.append([])
        for j in range(len(array[0])):
            result[i].append(min(max(array[i][j], min_value), max_value))
    return result

def shift(array, shift_value):
    """
    Прибавить к изображению константу shift_value.
    array: двумерный массив
    shift_value: величина сдвига
    result: двумерный массив
    """
    result = []
    for i in range(len(array)):
        result.append([])
        for j in range(len(array[0])):
            result[i].append(array[i][j] + shift_value)
    return result

def normalize(array, min_value, max_value):
    pass