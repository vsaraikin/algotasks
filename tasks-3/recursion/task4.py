# line = [3, 3, 3, 0, 1, 1, 1]
line = [1, 3, 4, 1, 2]




n, m = 0, len(line) - 1

common = []


class Solution:
    def __init__(self) -> None:
        self.counter = 0
        self.flag = False
    
    def F(self, n ,m):
        # print(n, m)
        self.counter += 1
        if self.flag:
            tmp_F = max(line[n], line[n+1])
            # common.append(tmp_F)
            return tmp_F
        else:
            return max(self.T(n+1, m), self.T(n, m-1))

    def T(self, n, m):
        # print(n, m)
        self.counter += 1
        if self.counter == len(line) - 1:
            self.flag = True
            tmp_T = min(line[n], line[n+1])    
            # common.append(tmp_T)
            return tmp_T
        else:
            return min(self.F(n+1, m), self.F(n, m-1))
    
    

s = Solution()        
s.F(n, m)

print(common)
        