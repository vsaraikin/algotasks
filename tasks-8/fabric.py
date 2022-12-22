# 2. Написать фабрику для данной иерархии. То есть, например, написать метод, который по параметру str_type возвращает объект нужного класса. Например, имеем входные данные str_type = „Square”, params = {x1=1, y1=1, x2=2, y2=2}. Должен быть создан соответствующий объект.

# Важные критерии:
# А) Нормальный нэйминг полей, методов и классов;
# Б) Указание типов и комментарии
# В) Минимум дубликации кода

from figures import * 
from abc import ABC, abstractmethod

str_type = "Square"
params = (0, 0, 0, 2, 3, 2, 3, 0)

class Fabric(ABC):
        
    def create_object(self) -> Figure:
        self.object = Figure()
        return self.object
    
    
class FabricFigure(Fabric):
    
    def create_object(self, str_type: str, params: dict) -> Figure:
        
        if str_type == "Square":
            return Sqaure(*params)
        elif str_type == "Rectungular":
            return Rectungular(*params)
        elif str_type == "Triangle":
            return Triangle(*params)
        elif str_type == "Line":
            return Line(*params)
        elif str_type == "Dot":
            return Dot(*params)
        elif str_type == "Circle":
            return Circle(*params)
        elif str_type == "Ellipse":
            return Ellipse(*params)
    

print(FabricFigure().create_object(str_type, params))