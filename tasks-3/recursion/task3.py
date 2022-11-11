n = 6

quantity_mosquitos = [1, 100, 3, 4, 1000, 0]

class MosqPath:
    def __init__(self) -> None:
        self.pos2 = n - 1 
        self.pos3 = n - 1
        self.res2 = []
        self.res3 = []
    
    def substractor(self, qty: list, steps: int, results: list, positions: int):
        """ Substracts every three steps """
        # print('self pos3 is',self.pos3)
        
        if len(qty) < 4:
            results.insert(0, qty[0])
            results.append(quantity_mosquitos[-1])
            return False
        
        results.insert(0, max(qty[positions - 2], qty[positions - 3]))
        positions -= steps
        
        return self.substractor(qty[:positions], steps, results, positions) and self.substractor(qty[:positions - 1], steps, results, positions)
    
        
    def best_spots(self, qty: list):
        self.substractor(qty, 2, self.res2, self.pos2)
        self.substractor(qty, 3, self.res3, self.pos3)
        
        indexes_two = [quantity_mosquitos.index(i) + 1 for i in self.res2]
        indexes_three = [quantity_mosquitos.index(i) + 1 for i in self.res2]
        
        if sum(self.res2) > sum(self.res3):
            return indexes_two
        else:
            return indexes_three
        
    
    
m = MosqPath()
print(m.best_spots(quantity_mosquitos))