def _rot90_cw(array):
    """
    Функция возвращает,повернутый на 90 градусов по часовой, двумерный массив
    array: двумерный массив
    result: двумерный массив
    """
    if (len(array) == 0):
        return []
    N, M = len(array[0]), len(array)
    result = []
    #нарисуй
    for i in range(N):
        new_row = []
        for j in range(M):
            new_row.append(array[M - 1 - j][i])
        result.append(new_row)
    return result

def _rot90_ccw(array):
    """
    Функция возвращает,повернутый на 90 градусов против часовой, двумерный массив
    array: двумерный массив
    result: двумерный массив
    """
    if (len(array) == 0):
        return []
    N, M = len(array[0]), len(array)
    result = []
    #нарисуй
    for i in range(N):
        new_row = []
        for j in range(M):
            new_row.append(array[j][N - 1 - i])
        result.append(new_row)
    return result

def rot(array, degree):
    """
    Функция возвращает,повернутый на заданное кол-во грудсов, двумерный массив
    array: двумерный массив
    degree: градусы
        90, 180, 270 -> на 90, 180, 270 по часовой стрелке
        -90, -180, -270 -> на 90, 180, 270 против часовой стрелки
    result: двумерный массив
    """
    positive_deg = {90,180,270}
    negative_deg = {-90,-180,-270}
    result = array
    if (degree not in positive_deg | negative_deg):
        raise RuntimeError("unsupported degree")
    elif (degree in positive_deg):
        for i in range(degree // 90):
            result = _rot90_cw(result)
    elif (degree in negative_deg):
        for i in range(degree // (-90)):
            result = _rot90_ccw(result)
    return result
