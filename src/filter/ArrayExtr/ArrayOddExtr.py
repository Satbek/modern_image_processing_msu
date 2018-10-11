from filter.ArrayExtr.base.ArrayExtr import ArrayExtr
class ArrayOddExtr(ArrayExtr):
    """
    Класс для четной экстраполяции
    3 2 1 | 1 2 3 | 3 2 1
    """
    @classmethod
    def is_extrapolation_for(cls, type_):
        return type_.lower() == 'odd'

    def __getitem__(self, key):
        if key >= 0 and key < len(self.body):
            if len(self.shape) == 1:
                return self.body[key]
            else:
                return ArrayOddExtr(self.body[key])

        elif key < 0:
            if len(self.shape) == 1:
                return self.body[abs(key) - 1]
            else:
                return ArrayOddExtr(self.body[abs(key) - 1])

        elif key >= len(self.body):
            new_pos = key - len(self.body)
            max_pos = len(self.body) - 1
            if max_pos - new_pos < 0:
                raise IndexError(self.__class__.__name__ + ": index out of range")
            if len(self.shape) == 1:
                return self.body[max_pos - new_pos]
            else:
                return ArrayOddExtr(self.body[max_pos - new_pos])
