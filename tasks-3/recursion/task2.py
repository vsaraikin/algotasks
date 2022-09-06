number_of_soliders = 31
threshold = [2, 3]


class Ways:
    def __init__(self) -> None:
        self.counter = 0

    def number_of_combinations(self, n: int) -> int:
        if n in threshold:
            self.counter += 1
            return self.counter
        
        else:
            return self.number_of_combinations(n // 2) and self.number_of_combinations((n + 1) // 2)
    
w = Ways()    
print(w.number_of_combinations(number_of_soliders))
