matrix = [
   # a, b, c, d
    [0, 1, 0, 0], # a 
    [1, 0, 0, 0], # b
    [0, 0, 0, 1], # c
    [0, 0, 1, 1], # d
]

matrix = [
   # a, b, c, d
    [0, 0, 0, 0], # a 
    [0, 0, 0, 0], # b
    [0, 0, 0, 0], # c
    [0, 0, 0, 0], # d
]

flag = 'yes'
for j in matrix:
    if sum(j) >  len(matrix) / 2:
        flag = 'no'
        break
    
all = {*range(len(matrix))}
known_list = set()
if flag == 'yes':
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if matrix[i][j] == 1:
                known_list.add(j)
    
    if len(known_list) == 1:
        known_list.add(all - known_list)
        
    elif len(known_list) == 0:
        known_list.add(0), known_list.add(len(matrix) - 1)


print(flag, {*range(len(matrix))} - known_list)