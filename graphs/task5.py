# --- Input ---

n, m, q = 4, 6, 6

connections = [
    (1, 2), (2, 3), (3, 4), (4, 1), (3, 1), (4, 2)
]
earthquakes = (1, 6, 2, 5, 4, 3)


# -------

con_eq = {k:v for k,v in zip(range(1, m + 1), connections)}

# C - C
# | x | this is how this graph looks on the schema
# C - C


# to make it incoherent, we need to delete n-1 connections = 3 in that case

peaks = {*range(1, n+1)}


def check_if_graph_coherent(graph: list):    
    
    unique_peaks = {city for connection in graph for city in connection}
    
    if peaks != unique_peaks:
        return False
    
    else:
        return True
    


for eq in earthquakes:
    con_eq.pop(eq)
    
    if check_if_graph_coherent(list(con_eq.values())):
        print(1, end='')
    else:
        print(0, end='')