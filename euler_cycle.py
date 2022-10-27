# we gonna check if each verticle has even number of edges

# not euler
# lines = [
#     (1, 0),
#     (0, 2),
#     (2, 1),
#     (0, 3),
#     (3, 4),
#     (1, 3)
# ]

# euler
lines = [
    (1, 0),
    (0, 2),
    (2, 1),
    (0, 3),
    (3, 4),
    (4, 0),
]


visited_d = {}

for edge in lines:
    if edge[0] not in visited_d.keys():
        visited_d[edge[0]] = 1
    else:
        visited_d[edge[0]] += 1
        
    if edge[1] not in visited_d.keys():
        visited_d[edge[1]] = 1
    else:
        visited_d[edge[1]] += 1
       
        
def check_euler_cycle(visited_d: dict):
    for n in visited_d.values():
        if n % 2 != 0:
            return False
        
    return True


print(check_euler_cycle(visited_d))