# line = [3, 3, 3, 0, 1, 1, 1]
# line = [2, 3, 100, 10, 1, 3] # -> 104
line = [1, 3, 4, 1, 2] # -> 6

n, m = 0, len(line) - 1

class Task:
   
    def F(self, n ,m):
        if m - n == 1:
            tmp_F = max(line[n] , line[n+1])
            return tmp_F
        else:
            return max(self.T(n+1, m) + line[n], self.T(n, m-1) + line[m])

    def T(self, n, m):
        if m - n == 1:
            tmp_T = min(line[n], line[n+1])    
            return tmp_T
        else:
            return min(self.F(n+1, m), self.F(n, m-1))
        

s = Task()        
print(s.F(n, m))