from filter.ArrayExtr.base.ArrayExtr import ArrayExtr
class ConstantArray:
    """Массив возвращающий одно и тоже значение"""
    def __init__(self, constant):
        self.constant = constant

    def __getitem__(self, key):
        return self.constant

class ArrayConstantExtr(ArrayExtr):
    """
    Класс для инициализации константой граничных пикслелей
    при экстраполяции
    const const const | 1 2 3 | const const const
    """
    def __init__(self, array, constant, by_ref = False):
        self.constant = constant
        #Массив из одного элемента, для 2д экстраполяции
        self.constant_array = ConstantArray(self.constant)
        super().__init__(array, by_ref)
        

    @classmethod
    def is_extrapolation_for(cls, type_):
        return type_.lower() == 'constant'

    def __getitem__(self, key):
        if key >= 0 and key < len(self.body):
            if len(self.shape) == 1:
                return self.body[key]
            else:
                return ArrayConstantExtr(self.body[key], self.constant, by_ref = True)
        elif key < 0:
            if len(self.shape) == 1:
                return self.constant
            else:
                return self.constant_array
        elif key >= len(self.body):
            if len(self.shape) == 1:
                return self.constant
            else:
                return self.constant_array
