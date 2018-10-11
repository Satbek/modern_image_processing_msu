class ArrayExtr:
    """
    Базовый класс для экстраполяции массива.
    """
    def __init__(self, array, by_ref = False):
        """
        array: экстраполируемый массив
        """
        if by_ref:
            self._body = array
        else:
            self._body = array[:]

    @property
    def shape(self):
        """
        Получить размерность массива
        array: одномерный или двумерный массив
        result: (dim1) or (dim1, dim2)
        """
        if type(self.body[0]) is list:
            return (len(self.body), len(self.body[0]))
        return (len(self.body),)
    

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
            return result
    raise ValueError("Unsupported extrapolation type : " + type_)