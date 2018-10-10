from filter.ArrayExtr.base.ArrayExtr import ArrayExtr
class ArrayRepExtr(ArrayExtr):
    """
    Класс для дублирования граничных пикселей
    при экстраполяции
    1 1 1 | 1 2 3 | 3 3 3
    """

    @classmethod
    def is_extrapolation_for(cls, type_):
        return type_.lower() == 'rep'

    #toDo продолжение вверх в 2d случае сделать и тесты написать
    def __getitem__(self, key):
        if key >= 0 and key < len(self.body):
            if len(self.shape) == 1:
                return self.body[key]
            else:
                return ArrayRepExtr(self.body[key])
        elif key < 0:
            if len(self.shape) == 1:
                return self.body[0]
            else:
                return ArrayRepExtr(self.body[0])
        elif key >= len(self.body):
            if len(self.shape) == 1:
                return self.body[-1]
            else:
                return ArrayRepExtr(self.body[-1])
