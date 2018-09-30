def _mirror_x(array):
    """
    Отражение по горизонтали
    array: двумерный массив
    result: двумерный массив
    """
    result = []
    for row in array:
        new_row = []
        for elem in reversed(row):
            new_row.append(elem)
        result.append(new_row)
    return result

def _mirror_y(array):
    """
    Отражение по вертикали
    array: двумерный массив
    result: двумерный массив
    """
    result = []
    for row in reversed(array):
        result.append(row)
    return result

def mirror(array, mode):
    """
    Отражение по горизонтали или по вертикали, в зависомсти от указанного параметра
    array: двумерный массив
    mode: параметр, x - по горизонтали, y - по вертикали
    result: двумерный массив
    """
    if mode == 'x':
        return _mirror_x(array)
    elif mode == 'y':
        return _mirror_y(array)
    else:
        raise RuntimeError
