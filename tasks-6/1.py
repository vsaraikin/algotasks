levels = []

n = 3 # -> 2 

# 1
# 1 1

# n = 4 # -> 2

# 1
# 1 1 1

# n = 5 # -> 2

# 1
# 1 1
# 1 1

# n = 6 # -> 3


def non_rec(n):
    
    s = 0
    for i in range(1, n):
        s += i

        if s == n:
            return i
        
        elif s > n:
            return i - 1
            
        

def rec(n, stair_lvl):
    if n < 0:
        return stair_lvl - 1
    elif n == 0:
        return stair_lvl
    
    else:
        stair_lvl += 1
        n -= stair_lvl
        return rec(n, stair_lvl)

print(non_rec(n))        
print(rec(n, 0))
