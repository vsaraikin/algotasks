verticles = 4

A = [[0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0]]

d = {}

"""
The easiest way:
|V| = |E| + 1 
"""

def func1(A):
    e = 0
    v = len(A)
    
    
    for i in range(0, len(A)):
        if A[i].count(0) == verticles:
            return "No"
        
        for j in range(i, len(A)):
            if A[i][j] == 1:
                e += 1
    
    if e + 1 == v:
        return "Yes"
    else:
        return "No"

print(func1(A))                





