# A: 5
# n, m = 5, 6 # graph vertices, graph verges
# graph = [
#     [1, 2, 2],
#     [2, 5, 5],
#     [2, 3, 4],
#     [5, 3, 1],
#     [1, 4, 1],
#     [4, 3, 3],
#     [3, 5, 1],
# ]

# n, m = 1, 0 # error
# A = []


# A: 1
n, m = 2, 6
graph = [
    [1, 2, 1],
    [1, 2, 2],
    [1, 2, 3],
    [1, 2, 4],
    [1, 2, 5],
    [1, 2, 6],
]


if n == 0 or m == 0:
    print("n or m cannot be zero")
    exit()


nodes = {x[0] for x in graph}.union({x[1] for x in graph}) # finding all of the verticles in graph

import heapq
from collections import defaultdict

def dijkstra(edges, start=1):
    
    # Changing data structure from 2-d list to dict
    graph = {}
    
    for edge in edges:
        if graph.get(edge[0]) is None:
            graph[edge[0]] = []
            
        graph[edge[0]].append((edge[1], edge[2]))
    
    path_lengths = {}
    heap = [(0, start)]
    
    while heap:
        dist, node = heapq.heappop(heap)
        
        if node in path_lengths:
            continue
        
        path_lengths[node] = dist
        
        if graph.get(node):
            for end_element, weight in graph[node]:
                if end_element not in path_lengths:
                    heapq.heappush(heap, (dist + weight, end_element))
                
    return path_lengths[max(nodes)]

print(dijkstra(graph))