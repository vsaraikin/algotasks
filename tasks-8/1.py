# 1. Написать иерархию классов для представления геометрических фигур.
# Фигуры: Точка, линия, треугольник, прямоугольник, квадрат, окружность, эллипс.
# Все классы должны принадлежать одной иерархии. Главный предок – абстрактный класс Figure.
# Методы: str_type.
# Property: вычисление периметра, площади.
# Поддерживаемые операции: str, +, -, * на int, ==, <, >, <=, >=.
# Нюансы:
# + и – для точек: средняя точка между ними
# + для линии – объединение линий, если они пересекаются, иначе вернуть первую
# - для линии – выкинуть пересекающуюся часть из от первой линии
# + для остальных фигур – берём одну опорную точку


from abc import ABC, abstractmethod
from typing import Tuple
from math import pi


class Figure(ABC):
    @abstractmethod
    def str_type(
        self,
    ):
        pass

    @abstractmethod
    def perimeter(
        self,
    ):
        pass

    @abstractmethod
    def square(
        self,
    ):
        pass


class Dot(Figure):
    """
    Simply a dot in a one-dimensional space
    """

    def __init__(self, x: int):
        self.x = x

    def str_type(self):
        return "Dot"

    def perimeter(self):
        return 0

    def square(self):
        return 0

    def __add__(self, term: int) -> int:
        return (self.x + term) / 2

    def __sub__(self, subtrahend: int) -> int:
        return (self.x - subtrahend) / 2

    def __mul__(self, mult: int):
        self.x *= mult
        return self.x

    def __truediv__(self, divider: int) -> float:
        self.x /= divider
        return self.x

    def __floordiv__(self, divider: int) -> int:
        self.x //= divider
        return self.x

    def __eq__(self, o: object) -> bool:
        return self.x == o

    def __lt__(self, other) -> bool:
        return self.x < other

    def __le__(self, other) -> bool:
        return self.x <= other

    def __gt__(self, other) -> bool:
        return self.x > other

    def __ge__(self, other) -> bool:
        return self.x >= other


class Line(Figure):
    """
    One-dimensional line which has start and finish points
    """

    def __init__(self, a, b):
        if a <= b:
            self.a = a
            self.b = b
        else:
            self.a = b
            self.b = a

    def str_type(self):
        return "Line"

    def perimeter(self):
        return self.b - self.a

    def square(self):
        return 0

    def __truediv__(self, divider: int) -> Tuple[float]:
        self.a /= divider
        self.b /= divider
        return self.a, self.b

    def __floordiv__(self, divider: int) -> Tuple[int]:
        self.a //= divider
        self.b //= divider
        return self.a, self.b

    def __eq__(self, o: Tuple[object, object]) -> bool:
        return (self.a, self.b) == (o[0], o[1])

    def __lt__(self, o: Tuple[object, object]) -> bool:
        return self.b - self.a < abs(o[1] - o[0])

    def __le__(self, o: Tuple[object, object]) -> bool:
        return self.b - self.a <= abs(o[1] - o[0])

    def __gt__(self, o: Tuple[object, object]) -> bool:
        return self.b - self.a > abs(o[1] - o[0])

    def __ge__(self, o: Tuple[object, object]) -> bool:
        return self.b - self.a >= abs(o[1] - o[0])


# o = Line(2, 3)
# print(o / 2)


class Triangle(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.a = self.calc_length(self.x1, self.y1, self.x2, self.y2)
        self.b = self.calc_length(self.x2, self.y2, self.x3, self.y3)
        self.c = self.calc_length(self.x1, self.y1, self.x3, self.y3)

    def calc_length(self, a1: int, b1: int, a2: int, b2: int) -> float:
        return pow(pow(a2 - a1, 2) + pow(b2 - b1, 2), 0.5)

    def error(self, obj: object):
        raise TypeError(obj)

    def get_corrdinates(
        self,
    ) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
        return ((self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3))

    def str_type(self):
        return "Triangle"

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def square(self) -> float:
        return pow(
            self.perimeter()
            / 2
            * (self.perimeter() / 2 - self.a)
            * (self.perimeter() / 2 - self.b)
            * (self.perimeter() / 2 - self.c),
            0.5,
        )

    def __add__(self, term: int) -> float:
        self.x2 += term
        self.y2 += term
        self.x3 += term
        self.y3 += term
        return self.get_corrdinates()

    def __sub__(self, subtrahend: int) -> float:
        self.x2 -= subtrahend
        self.y2 -= subtrahend
        self.x3 -= subtrahend
        self.y3 -= subtrahend
        return self.get_corrdinates()

    def __mul__(self, mult: int) -> float:
        self.x2 -= mult
        self.y2 -= mult
        self.x3 -= mult
        self.y3 -= mult
        return self.get_corrdinates()

    def __truediv__(self, divider: int) -> float:
        self.x2 /= divider
        self.y2 /= divider
        self.x3 /= divider
        self.y3 /= divider
        return self.get_corrdinates()

    def __floordiv__(self, divider: int) -> float:
        self.x2 //= divider
        self.y2 //= divider
        self.x3 //= divider
        self.y3 //= divider
        return self.get_corrdinates()

    def __eq__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) == self.square(o)

    def __lt__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) < self.square(o)

    def __le__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) <= self.square(o)

    def __gt__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) > self.square(o)

    def __ge__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) >= self.square(o)


# tr = Triangle(1, 1, 3, 4, 3, 1)

# print(tr.perimeter())


class Rectungular(Figure):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self.a = self.calc_length(self.x1, self.y1, self.x2, self.y2)
        self.b = self.calc_length(self.x2, self.y2, self.x3, self.y3)
        self.c = self.calc_length(self.x4, self.y4, self.x3, self.y3)
        self.d = self.calc_length(self.x1, self.y1, self.x4, self.y4)

    def calc_length(self, a1: int, b1: int, a2: int, b2: int) -> float:
        return pow(pow(a2 - a1, 2) + pow(b2 - b1, 2), 0.5)

    def error(self, obj: object):
        raise TypeError(obj)

    def get_corrdinates(
        self,
    ) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
        return (
            (self.x1, self.y1),
            (self.x2, self.y2),
            (self.x3, self.y3),
            (self.x4, self.y4),
        )

    def str_type(self):
        return "Rectungular"

    def perimeter(self) -> float:
        return self.a + self.b + self.c + self.d

    def square(self) -> float:
        return self.a * self.b

    def __add__(self, term: int) -> float:
        self.x2 += term
        self.y2 += term
        self.x3 += term
        self.y3 += term
        self.x4 = self.b + self.x1
        self.y4 = self.a + self.y1

        return self.get_corrdinates()

    def __sub__(self, subtrahend: int) -> float:
        self.x2 -= subtrahend
        self.y2 -= subtrahend
        self.x3 -= subtrahend
        self.y3 -= subtrahend
        self.x4 = self.b - self.x1
        self.y4 = self.a - self.y1

        return self.get_corrdinates()

    def __mul__(self, mult: int) -> float:
        self.x2 *= mult
        self.y2 *= mult
        self.x3 *= mult
        self.y3 *= mult
        self.x4 = self.b - self.x1
        self.y4 = self.a - self.y1

        return self.get_corrdinates()

    def __truediv__(self, divider: int) -> float:
        self.x2 /= divider
        self.y2 /= divider
        self.x3 /= divider
        self.y3 /= divider
        self.x4 = self.b - self.x1
        self.y4 = self.a - self.y1

        return self.get_corrdinates()

    def __floordiv__(self, divider: int) -> float:
        self.x2 //= divider
        self.y2 //= divider
        self.x3 //= divider
        self.y3 //= divider
        self.x4 = self.b - self.x1
        self.y4 = self.a - self.y1

        return self.get_corrdinates()

    def __eq__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) == self.square(o)

    def __lt__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) < self.square(o)

    def __le__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) <= self.square(o)

    def __gt__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) > self.square(o)

    def __ge__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) >= self.square(o)


class Sqaure(Rectungular):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3, x4, y4)

    def str_type(self):
        return "Sqaure"


class Circle(Figure):
    def __init__(self, r: int, x: int, y: int):
        self.r = r
        self.x = x
        self.y = y

    def calc_length(self, a1: int, b1: int, a2: int, b2: int) -> float:
        return pow(pow(a2 - a1, 2) + pow(b2 - b1, 2), 0.5)

    def error(self, obj: object):
        raise TypeError(obj)

    def get_corrdinates(
        self,
    ) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
        return (
            (self.x1, self.y1),
            (self.x2, self.y2),
            (self.x3, self.y3),
            (self.x4, self.y4),
        )

    def str_type(self):
        return "Circle"

    def perimeter(self) -> float:
        return 2 * pi * self.r

    def square(self) -> float:
        return self.r * pi**2

    def __add__(self, term: int) -> float:
        self.r += term

        return self.get_corrdinates()

    def __sub__(self, subtrahend: int) -> float:
        self.r -= subtrahend

        return self.get_corrdinates()

    def __mul__(self, mult: int) -> float:
        self.r *= mult

        return self.get_corrdinates()

    def __truediv__(self, divider: int) -> float:
        self.r /= divider

        return self.get_corrdinates()

    def __floordiv__(self, divider: int) -> float:
        self.r //= divider

        return self.get_corrdinates()

    def __eq__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) == self.square(o)

    def __lt__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) < self.square(o)

    def __le__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) <= self.square(o)

    def __gt__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) > self.square(o)

    def __ge__(
        self, o: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]
    ) -> bool:
        return self.square(self.get_corrdinates()) >= self.square(o)


class Ellipse(Circle):
    def __init__(self, r1: int, r2: int, x: int, y: int):
        self.r1 = r1
        self.r2 = r2
        self.x = x
        self.y = y

    def error(self, obj: object):
        raise TypeError(obj)

    def get_corrdinates(
        self,
    ) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
        return (
            (self.x1, self.y1),
            (self.x2, self.y2),
            (self.x3, self.y3),
            (self.x4, self.y4),
        )

    def str_type(self):
        return "Circle"

    def perimeter(self) -> float:
        return 2 * pi * pow((self.r1 + self.r2) / 2, 0.5)

    def square(self) -> float:
        return self.r1 * self.r2 * pi

    def __add__(self, term: int) -> float:
        self.r += term

        return self.get_corrdinates()

    def __sub__(self, subtrahend: int) -> float:
        self.r -= subtrahend

        return self.get_corrdinates()

    def __mul__(self, mult: int) -> float:
        self.r *= mult

        return self.get_corrdinates()

    def __truediv__(self, divider: int) -> float:
        self.r /= divider

        return self.get_corrdinates()

    def __floordiv__(self, divider: int) -> float:
        self.r //= divider

        return self.get_corrdinates()
