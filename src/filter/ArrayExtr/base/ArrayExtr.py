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

def GetArrayExtr(array, type_):
    """
    Возвращает нужный класс для экстраполяции.
    array: экстраполируемый массив
    type_: тип экстраполяции
    result: экземпляр класса для экстраполяции
    """
    for cls in ArrayExtr.__subclasses__():
        if cls.is_extrapolation_for(type_):
            return cls(array)
    raise ValueError("Unsupported extrapolation type : " + type_)