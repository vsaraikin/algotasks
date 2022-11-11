n = 7

# A = [
#     [0, 1, 1, 0, 0, 0, 0],
#     [0, 0, 0, 0, 1, 0, 0],
#     [0, 1, 0, 1, 1, 0, 0],
#     [0, 1, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 0]
# ]

n = 4
A = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]

# import queue
visited = set()
visited_list = []
queue = []

def bfs(node):
    visited.add(node)
    visited_list.append(node)
    queue.append(node)
    
    while queue:
        tmp = queue.pop(0)
        
        slice = A[tmp]
        for i in range(n):
            if slice[i] == 1 and i not in visited:
                visited.add(i)
                visited_list.append(i)
                queue.append(i)
                

bfs(0)

all_peaks = set(range(0, n)) 

# there are peaks that did not have path to them, but we still should include them
not_included = all_peaks - visited

for i in not_included:
    visited_list.append(i)
    
    
visited_list = [x + 1 for x in visited_list]
print(visited_list)

                