# check if graph is coherent

n, m, q = 4, 6, 6

connections = [
    (1, 2), (2, 3), (3, 4), (4, 1), (3, 1), (4, 2)
]
earthquakes = (1, 6, 2, 5, 4, 3)

con_eq = {k:v for k,v in zip(earthquakes, connections)}

# C - C
# | x | this is how this graph looks on the schema
# C - C


# to make it incoherent, we need to delete n-1 connections = 3 in that case


def make_slice(i: list, graph: list):
    return [city for connection in graph[i+1:] for city in connection]

def check_if_graph_coherent(graph: list):    
    
    for c in range(len(graph)):
        
        slice = make_slice(c, graph)

        if (graph[c][0] not in slice) and (graph[c][1] not in slice):
            return False
    
        else:
            return True


for eq in earthquakes:
    con_eq.pop(eq)
    
    if check_if_graph_coherent(list(con_eq.values())):
        print(1, end='')
    else:
        print(0, end='')