A = [
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0]
]

visited = set()

def bfs():

    for i in range(len(A)):
        for x in range(len(A)):        
            if A[i][x] == 1:
                
                if i + 1 not in visited:  
                    visited.add(i + 1)
                if x + 1 not in visited: 
                    visited.add(x + 1)
            
bfs()            
print(visited)