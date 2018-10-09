from filter.ArrayExtr.base.ArrayExtr import ArrayExtr
class ArrayConstantExtr(ArrayExtr):
    """
    Класс для инициализации константой граничных пикслелей
    при экстраполяции
    const const const | 1 2 3 | const const const
    """
    def __init__(self, array, constant):
        self.constant = constant
        super().__init__(array)

    @classmethod
    def is_extrapolation_for(cls, type_):
        return type_.lower() == 'constant'

    def __getitem__(self, key):
        if key >= 0 and key < len(self.body):
            if len(self.shape) == 1:
                return self.body[key]
            else:
                return ArrayConstantExtr(self.body[key], self.constant)
        elif key < 0:
            if len(self.shape) == 1:
                return self.constant
            else:
                return ArrayConstantExtr([self.constant] * self.shape[1], self.constant)
        elif key >= len(self.body):
            if len(self.shape) == 1:
                return self.constant
            else:
                return ArrayConstantExtr([self.constant] * self.shape[1], self.constant)
