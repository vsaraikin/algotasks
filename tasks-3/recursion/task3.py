n = 6

quantity_mosquitos = [1, 100, 3, 4, 1000, 0]

class MosqPath:
    def __init__(self) -> None:
        self.pos2 = n - 1 
        self.pos3 = n - 1
        self.res2 = []
        self.res3 = []

    
    def two(self, qty: list):
        """ Substracts every two steps """
        # print('self pos2 is' ,self.pos2)
        
        if len(qty) < 4:
            self.res2.insert(0, qty[0])
            self.res2.append(quantity_mosquitos[-1])
            return False
        
        self.res2.insert(0, max(qty[self.pos2 - 2], qty[self.pos2 - 3]))
        self.pos2 -= 2
        
        return self.two(qty[:self.pos2]) and self.two(qty[:self.pos2 - 1])
    
    
    def three(self, qty: list):
        """ Substracts every three steps """
        # print('self pos3 is',self.pos3)
        
        if len(qty) < 4:
            self.res3.insert(0, qty[0])
            self.res3.append(quantity_mosquitos[-1])
            return False
        
        self.res3.insert(0, max(qty[self.pos3 - 2], qty[self.pos3 - 3]))
        self.pos3 -= 3
        
        return self.three(qty[:self.pos3]) and self.three(qty[:self.pos3 - 1])
    
    def best_spots(self, qty: list):
        self.two(qty)
        self.three(qty)
        
        indexes_two = [quantity_mosquitos.index(i) + 1 for i in self.res2]
        indexes_three = [quantity_mosquitos.index(i) + 1 for i in self.res2]
        
        if sum(self.res2) > sum(self.res3):
            return indexes_two
        else:
            return indexes_three
        
    
    
m = MosqPath()
print(m.best_spots(quantity_mosquitos))