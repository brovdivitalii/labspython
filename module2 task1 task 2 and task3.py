class TRTriangle:
    """
    Класс рівностороннього трикутника.
    """

    def __init__(self, *args: float):
        if len(args) == 0:
            self.__a = 0
        elif len(args) == 1:
            self.__a = args[0]
        else:
            raise Exception('Data is not correct')

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    def Area(self):
        return ((self.__a ** 2) * (3 ** 1 / 2)) / 4

    def P(self):
        return self.__a * 3

    def is_equal(self, other):
        eps = 0.000000001
        if abs(self.__a - other.a) < eps:
            print('True')
        else:
            print('False')

    def __add__(self, other):
        return TRTriangle(self.__a + other.a)

    def __sub__(self, other):
        return TRTriangle(self.a - other.a)

    def __mul__(self, other):
        return self.__a * other.a


class TPiramid(TRTriangle):
    def __init__(self, *args: float):
        super(TPiramid, self).__init__()
        self.__h = args[1]

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, value):
        self.__h = value

    def Volume(self):
        return (1 / 3) * self.__h * (super().a ** 2)


a = TRTriangle(7)
print(a.Area())
print(a.P())
b = TPiramid(4,5)
print(b.Volume())
