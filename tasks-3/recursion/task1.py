n = 2
m = 2


class Ways:
    def __init__(self) -> None:
        self.counter = 0
        

    def number_of_ways(self, a: int, b: int) -> int:
        if a == 1 or b == 1:
            self.counter += 1
            return self.counter
        
        return self.number_of_ways(a-1, b) and self.number_of_ways(a, b-1)

w = Ways()
print(w.number_of_ways(n, m))
