A = [
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0]
]

    
visited = []


def dfs(node):

    visited.append(node)
    for i in range(len(A)):
        if A[node][i] == 1 and i not in visited:
            dfs(i)
            
dfs(0)
print([x + 1 for x in visited])