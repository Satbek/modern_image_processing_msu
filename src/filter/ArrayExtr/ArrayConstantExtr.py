from filter.ArrayExtr.base.ArrayExtr import ArrayExtr
class ArrayConstantExtr(ArrayExtr):
    """
    Класс для инициализации константой граничных пикслелей
    при экстраполяции
    1 1 1 | 1 2 3 | 3 3 3
    """
    def __init__(self, array, constant):
        self.constant = constant
        super().__init__(array)

    @classmethod
    def is_extrapolation_for(cls, type_):
        return type_.lower() == 'constant'

    def __getitem__(self, key):
        if key >= 0 and key < len(self.body):
            return self.body[key]
        elif key < 0:
            return self.constant
        elif key >= len(self.body):
            return self.constant