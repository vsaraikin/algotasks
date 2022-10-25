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
edges = {(k[0], k[1]):k[2] for k in graph}
    

def find_best_clones(graph):
    unique_graph = {}

    for i in range(len(graph)):

        if unique_graph.get((graph[i][0], graph[i][1])) is None:
            unique_graph[(graph[i][0], graph[i][1])] = graph[i][2]

        else:
            current_value = unique_graph[(graph[i][0], graph[i][1])]
            if graph[i][2] < current_value:
                unique_graph[(graph[i][0], graph[i][1])] = current_value
        
    unique_graph = [(*x[0], x[1]) for x in unique_graph.items()]
            
    return unique_graph

# there is a corner case, when there are several connections with the same start and end points
# we have to choose the smallest of them
if len(edges) != len(graph):
    graph = find_best_clones(graph)
    edges = {(k[0], k[1]):k[2] for k in graph}



def dijkstra(nodes, edges, start=1):
    """ Shortest path """
    
    path_lengths = {v:float('inf') for v in nodes}
    path_lengths[start] = 0
    
    adj_nodes = {v:{} for v in nodes}
    
    for (u, v), weight in edges.items():
        adj_nodes[u][v] = weight
        adj_nodes[v][u] = weight
        
    temp_nodes = [v for v in nodes]
    
    while len(temp_nodes) > 0:
        upper_bounds = {v: path_lengths[v] for v in temp_nodes}
        u = min(upper_bounds, key=upper_bounds.get)
        temp_nodes.remove(u)
        
        for v, weight in adj_nodes[u].items():
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + weight)
            
    return path_lengths[max(nodes)]
    
    
print(dijkstra(nodes, edges))