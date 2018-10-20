from filter.ArrayExtr.base.ArrayExtr import ArrayExtr
class ArrayOddExtr(ArrayExtr):
    """
    Класс для нечетной экстраполяции
    -1 0 1 | 1 2 3 | 3 4 5
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
                return 2 * self.body[0] - self.body[-1 * key - 1]
            else:
                return ArrayOddExtr([i[0] - i[1] for i in zip([2 * i for i in self.body[0]], self.body[-1 * key - 1])])
        elif key >= len(self.body):
            max_pos = len(self.body) - 1
            new_pos = 2 * max_pos - key + 1
            if new_pos < 0:
                raise IndexError(self.__class__.__name__ + ": index out of range")
            if len(self.shape) == 1:
                return 2 * self.body[max_pos] - self.body[new_pos]
            else:
                return ArrayOddExtr([i[0] - i[1] for i in zip([2 * i for i in self.body[max_pos]], self.body[new_pos])])
