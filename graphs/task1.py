
paths = [
    [3, 2], # 0 1 0
    [1, 2], # 1 0 1
    [2, 3]  # 0 1 0
]

paths = [
    [4, 3], # 0 1 1 0
    [1, 2], # 1 0 0 1
    [1, 3], # 1 0 0 0
    [2, 4]  # 0 1 0 0
]

matrix = [[0] * len(paths) for _ in range(len(paths))]
paths = sorted([(path[0] - 1, path[1] - 1) for path in paths])

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if (i, j) in paths:
            matrix[i][j] = 1
        elif (j, i) in paths:
            matrix[i][j] = 1
            
for line in matrix:
    print(line)