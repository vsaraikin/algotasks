# INPUT

n, m = [int(x) for x in input().split()]

paths = []

for _ in range(m):
    paths.append([int(x) for x in input().split()])


matrix = [[0] * len(paths) for _ in range(n)]
paths = sorted([(path[0] - 1, path[1] - 1) for path in paths])

for i in range(n):
    for j in range(m):
        if (i, j) in paths:
            matrix[i][j] = 1
        elif (j, i) in paths:
            matrix[i][j] = 1
            
for line in matrix:
    print(line)