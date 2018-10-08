class ArrayExtr:
    """
    Базовый класс для экстраполяции массива.
    """
    def __init__(self, array):
        """
        array: экстраполируемый массив
        """
        self._body = array[:]

    @property
    def body(self):
        return self._body
    
    def __getitem__(self, key):
        raise RuntimeError("Not implemented")

    def __len__(self):
        return len(self.body)

def GetArrayExtr(array, type_, *args, **kwargs):
    """
    Возвращает нужный класс для экстраполяции.
    array: экстраполируемый массив (одномерный или двумерны массив)
    type_: тип экстраполяции
    *args, **kwargs: дополнительные параметры для экстрполяции
    result: экземпляр класса для экстраполяции
    """
    for cls in ArrayExtr.__subclasses__():
        if cls.is_extrapolation_for(type_):
            result = cls(array, *args, **kwargs)
            if type(array[0]) is list:
                for row in array:
                    row[:] = cls(row, *args, **kwargs)
            return result
    raise ValueError("Unsupported extrapolation type : " + type_)