n = 7

A = [
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0]
]

visited = set() # for checking visited peaks O(1)
visited_list = [] # for displaying visited peaks 

def dfs(node):
    if node not in visited:
        
        visited.add(node)
        visited_list.append(node + 1)
        
        slice = A[node]
        
        for i in range(n):
            if slice[i] == 1:
                dfs(i)
            
dfs(0)

all_peaks = set(range(0, n)) 

# there are peaks that did not have path to them, but we still should include them
not_included = all_peaks - visited 

for i in not_included:
    visited_list.append(i + 1)
    
print(visited_list)
