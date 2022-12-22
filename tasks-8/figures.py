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
    def str_type(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass


class Dot(Figure):
    """
    a dot in a one-dimensional space
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

    def __lt__(self, other: int) -> bool:
        return self.x < other

    def __le__(self, other: int) -> bool:
        return self.x <= other

    def __gt__(self, other: int) -> bool:
        return self.x > other

    def __ge__(self, other: int) -> bool:
        return self.x >= other




class Line(Figure):
    """
    one-dimensional line which has start and finish points
    """

    def __init__(self, a: int, b: int):
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

    def __add__(self, term: int) -> int:
        return (self.b + term) / 2

    def __sub__(self, subtrahend: int) -> int:
        return (self.b - subtrahend) / 2

    def __mul__(self, mult: int):
        self.b *= mult
        return self.b

    def __truediv__(self, divider: int) -> Tuple[float]:
        self.b /= divider
        return self.a, self.b

    def __floordiv__(self, divider: int) -> Tuple[int]:
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



class Triangle(Figure):
    
    """
    triangle in 2-dimensional space with 3 coordinates
    """
    
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self._a = self._calc_length(self.x1, self.y1, self.x2, self.y2)
        self._b = self._calc_length(self.x2, self.y2, self.x3, self.y3)
        self._c = self._calc_length(self.x1, self.y1, self.x3, self.y3)
        

    def _calc_length(self, a1: int, b1: int, a2: int, b2: int) -> float:
        return pow(pow(a2 - a1, 2) + pow(b2 - b1, 2), 0.5)

    def error(self, obj: object):
        raise TypeError(obj)

    def get_corrdinates(
        self,
    ) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
        return ((self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3))

    def str_type(self):
        return "Triangle"

    def _perimeter(self, a: int, b: int, c: int) -> float:
        return a + b + c

    def _square(self, a: int, b: int, c: int) -> float:
        P = self._perimeter(a, b, c)
        return pow(
            P / 2
            * (P / 2 - a)
            * (P / 2 - b)
            * (P / 2 - c),
            0.5,
        )
        
    @property
    def perimeter(self) -> float:
        return Triangle._perimeter(self, self._a, self._b, self._c)
    
    @property
    def square(self) -> float:
        return Triangle._square(self, self._a, self._b, self._c)

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

    def __eq__(self, object: Tuple[int]) -> float:
        x1, y1, x2, y2, x3, y3 = object
        a = self._calc_length(x1, y1, x2, y2)
        b = self._calc_length(x2, y2, x3, y3)
        c = self._calc_length(x1, y1, x3, y3)
        return self.square == self._square(a, b, c)

    def __lt__(self, object: Tuple[int]) -> float:
        x1, y1, x2, y2, x3, y3 = object
        a = self._calc_length(x1, y1, x2, y2)
        b = self._calc_length(x2, y2, x3, y3)
        c = self._calc_length(x1, y1, x3, y3)
        return self.square < self._square(a, b, c)


    def __le__(self, object: Tuple[int]):
        x1, y1, x2, y2, x3, y3 = object
        a = self._calc_length(x1, y1, x2, y2)
        b = self._calc_length(x2, y2, x3, y3)
        c = self._calc_length(x1, y1, x3, y3)
        return self.square <= self._square(a, b, c)

    def __gt__(self, object: Tuple[int]):
        x1, y1, x2, y2, x3, y3 = object
        a = self._calc_length(x1, y1, x2, y2)
        b = self._calc_length(x2, y2, x3, y3)
        c = self._calc_length(x1, y1, x3, y3)
        return self.square > self._square(a, b, c)

    def __ge__(self, object: Tuple[int]):
        x1, y1, x2, y2, x3, y3 = object
        a = self._calc_length(x1, y1, x2, y2)
        b = self._calc_length(x2, y2, x3, y3)
        c = self._calc_length(x1, y1, x3, y3)
        return self.square >= self._square(a, b, c)





class Rectungular(Figure):
    
    """
    rectungular in 2-dimensional space with 4 coordinates
    """
    
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        self._a = self._calc_length(self.x1, self.y1, self.x2, self.y2)
        self._b = self._calc_length(self.x1, self.y1, self.x3, self.y3)
        

    def _calc_length(self, a1: int, b1: int, a2: int, b2: int) -> float:
        return pow(pow(a2 - a1, 2) + pow(b2 - b1, 2), 0.5)

    def error(self, obj: object):
        raise TypeError(obj)

    def get_corrdinates(
        self,
    ) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
        return ((self.x1, self.y1), (self.x2, self.y2), (self.x3, self.y3), (self.x4, self.y4))

    def str_type(self):
        return "Rectungular"

    def _perimeter(self, a: int, b: int) -> float:
        return a + b

    def _square(self, a: int, b: int) -> float:
        return a * b
        
    @property
    def perimeter(self) -> float:
        return Rectungular._perimeter(self, self._a, self._b)
    
    @property
    def square(self) -> float:
        return Rectungular._square(self, self._a, self._b)

    def __add__(self, term: int) -> float:
        self.y2 += term
        self.x3 += term
        self.x4 += term
        self.y4 += term 
        return self.get_corrdinates()

    def __sub__(self, subtrahend: int) -> float:
        self.y2 -= subtrahend
        self.x3 -= subtrahend
        self.x4 -= subtrahend
        self.y4 -= subtrahend
        return self.get_corrdinates()

    def __mul__(self, mult: int) -> float:
        self.y2 *= mult
        self.x3 *= mult
        self.x4 *= mult
        self.y4 *= mult 
        return self.get_corrdinates()

    def __truediv__(self, divider: int) -> float:
        self.y2 /= divider
        self.x3 /= divider
        self.x4 /= divider
        self.y4 /= divider 
        return self.get_corrdinates()

    def __floordiv__(self, divider: int) -> float:
        self.y2 //= divider
        self.x3 //= divider
        self.x4 //= divider
        self.y4 //= divider 
        return self.get_corrdinates()

    def __eq__(self, object: Tuple[int]) -> bool:
        x1, y1, x2, y2, x3, y3 = object
        a = self._calc_length(x1, y1, x2, y2)
        b = self._calc_length(x1, y1, x3, y3)
        return self.square == self._square(a, b,)

    def __lt__(self, object: Tuple[int])  -> bool:
        x1, y1, x2, y2, x3, y3 = object
        a = self._calc_length(x1, y1, x2, y2)
        b = self._calc_length(x1, y1, x3, y3)
        return self.square < self._square(a, b,)

    def __le__(self, object: Tuple[int]) -> bool:
        x1, y1, x2, y2, x3, y3 = object
        a = self._calc_length(x1, y1, x2, y2)
        b = self._calc_length(x1, y1, x3, y3)
        return self.square <= self._square(a, b,)

    def __gt__(self, object: Tuple[int]) -> bool:
        x1, y1, x2, y2, x3, y3 = object
        a = self._calc_length(x1, y1, x2, y2)
        b = self._calc_length(x1, y1, x3, y3)
        return self.square > self._square(a, b,)

    def __ge__(self, object: Tuple[int]) -> bool:
        x1, y1, x2, y2, x3, y3 = object
        a = self._calc_length(x1, y1, x2, y2)
        b = self._calc_length(x1, y1, x3, y3)
        return self.square >= self._square(a, b,)



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


    def error(self, obj: object):
        raise TypeError(obj)

    def get_corrdinates(self) -> Tuple[int]:
        return (
            (self.x - self.r, self.y),
            (self.x, self.r + self.y),
            (self.x + self.r, self.y),
            (self.x, self.x - self.r)
        )

    def str_type(self):
        return "Circle"

    def _perimeter(self, r: int) -> float:
        return 2 * pi * r

    def _square(self, r: int) -> float:
        return r * pi**2
    
    @property
    def perimeter(self) -> float:
        return self._perimeter(self.r)

    @property
    def square(self) -> float:
        return self._square(self.r)
    
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
        self.r /= divider
        return self.get_corrdinates()

    def __eq__(self, object: int) -> bool:
        return self.square == self._square(object)

    def __lt__(self, object: int) -> bool:
        return self.square < self._square(object)

    def __le__(self, object: int) -> bool:
        return self.square <= self._square(object)

    def __gt__(self, object: int) -> bool:
        return self.square > self._square(object)

    def __ge__(self, object: int) -> bool:
        return self.square >= self._square(object)



class Ellipse(Circle):
    
    def __init__(self, r1: int, r2: int, x: int, y: int):
        self.r1 = r1
        self.r2 = r2
        self.x = x
        self.y = y

    def error(self, obj: object):
        raise TypeError(obj)

    def get_corrdinates(self) -> Tuple[int]:
        return (
            (self.x - self.r1, self.y),
            (self.x, self.r2 + self.y),
            (self.x + self.r1, self.y),
            (self.x, self.y - self.r2)
        )

    def str_type(self):
        return "Ellipse"

    def _perimeter(self, r1: int, r2: int) -> float:
        return 2 * pi * pow((r1 + r2) / 2, 0.5)

    def _square(self, r1: int, r2: int) -> float:
        return r1 * r2 * pi
     
    @property
    def perimeter(self) -> float:
        return self._perimeter(self.r1, self.r2)

    @property
    def square(self) -> float:
        return self._square(self.r1, self.r2)

    def __add__(self, term: int) -> float:
        self.r1 += term
        self.r2 += term
        return self.get_corrdinates()

    def __sub__(self, subtrahend: int) -> float:
        self.r1 -= subtrahend
        self.r2 -= subtrahend
        return self.get_corrdinates()

    def __mul__(self, mult: int) -> float:
        self.r1 *= mult
        self.r2 *= mult
        return self.get_corrdinates()

    def __truediv__(self, divider: int) -> float:
        self.r1 /= divider
        self.r2 /= divider
        return self.get_corrdinates()

    def __floordiv__(self, divider: int) -> float:
        self.r1 //= divider
        self.r2 //= divider
        return self.get_corrdinates()

    def __eq__(self, object: Tuple[int]) -> bool:
        return self.square == self._square(object[0], object[1])

    def __lt__(self, object: Tuple[int]) -> bool:
        return self.square < self._square(object[0], object[1])

    def __le__(self, object: Tuple[int]) -> bool:
        return self.square <= self._square(object[0], object[1])

    def __gt__(self, object: Tuple[int]) -> bool:
        return self.square > self._square(object[0], object[1])

    def __ge__(self, object: Tuple[int]) -> bool:
        return self.square >= self._square(object[0], object[1])


if __name__ == '__main__':
    dot = Dot(1)
    print(dot + 2)
    print(dot * 2)
    print(dot >= 2)


    o = Line(2, 3)
    print(o * 2)
    print(o / 2)


    tr = Triangle(1, 1, 3, 4, 3, 1)
    print(tr + 2)
    print(tr.perimeter)
    print(tr.square)
    print(tr == (1, 1, 3, 4, 3, 1))

    rec = Rectungular(0, 0, 0, 2, 3, 2, 3, 0)
    print(rec.perimeter)
    print(rec.square)
    print(rec > (0, 0, 0, 2, 3, 2))

    sq = Sqaure(0, 0, 0, 2, 3, 2, 3, 0)
    print(sq.perimeter)
    print(sq.square)
    print(sq < (0, 0, 1, 1, 1, 1))
    print(sq.str_type())

    c = Circle(4, 1, 1)
    print(c.square)
    print(c.perimeter)
    print(c >= 2)


    e = Ellipse(4, 2, 1, 1)
    print(e.square)
    print(e.perimeter)
    print(e >= (2, 1))
