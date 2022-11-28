n = 2126753390

pick = 1702766719

def guess(i):
    if i < pick:
        return -1
    elif i > pick:
        return 1
    else:
        return 0

class Solution:

    def guessNumber(self, n: int) -> int:
        
        steps = [pow(10, p) for p in range(len(str(n)), 0, -1)]

        last_i = 1

        for step in steps:
            for i in range(last_i, n, step):
                    
                res = guess(i)
                # print(step, i, res)
                if res < 0:
                    last_i = i
                    pass
                
                elif res > 0:
                    break
                
                elif res == 0:
                    return i
                    
        for i in range(last_i, last_i+step):
            res = guess(i)
            
            if res == 0:
                return i
            
s = Solution()
print(s.guessNumber(n))