matrix = [
   # a, b, c, d, e
    [0, 1, 1, 0, 0], # a 
    [1, 0, 1, 0, 1], # b
    [1, 1, 0, 1, 0], # c
    [0, 0, 1, 0, 0], # d
    [0, 1, 0, 0, 0], # e
]

# matrix = [
#    # a, b, c, d
#     [0, 1, 0, 0], # a 
#     [1, 0, 0, 0], # b
#     [0, 0, 0, 1], # c
#     [0, 0, 1, 0], # d
# ]

# a -> b -> c

res = []


for i in range(len(matrix)):
    for j in range(i, len(matrix)):
        if matrix[i][j] == 1:
            res.append((i, j))
print(res)



d = set()
for pair_i in range(0, len(res)):
    for pair_j in range(pair_i + 1, len(res)):
        if res[pair_i][0] or res[pair_i][1] in res[pair_j]:
            d.add(res[pair_i][0])
            d.add(res[pair_i][1])
            d.add(res[pair_j][0])
            d.add(res[pair_j][1])
            

if len(d) == len(matrix):
    print('yes')
    
else:
    print('no')
