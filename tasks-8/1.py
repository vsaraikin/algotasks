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

class Figure(ABC):
    
    @abstractmethod
    def str_type(self,):
        pass
    
    @abstractmethod
    def perimeter(self,):
        pass
    
    @abstractmethod
    def square(self,):
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
        return (self.x + term)/2
    
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
        return self.b - self.a < abs(o[1]-o[0])
    
    def __le__(self, o: Tuple[object, object]) -> bool:
        return self.b - self.a <= abs(o[1]-o[0])
    
    def __gt__(self, o: Tuple[object, object]) -> bool:
        return self.b - self.a > abs(o[1]-o[0])
    
    def __ge__(self, o: Tuple[object, object]) -> bool:
        return self.b - self.a >= abs(o[1]-o[0])

o = Line(2, 3)
print(o <= (5,3))