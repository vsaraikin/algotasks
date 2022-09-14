matrix = [
    [1,   2,   3],
    [0.4, 1,   2],
    [0.5, 0.5, 1]
]

# matrix = [
#     [1, 1, 1],
#     [1, 1, 1],
#     [1, 1, 1]
# ]

flag = "No"
for i in range(len(matrix)):
    for j in range(i, len(matrix)):
        if matrix[i][j] == 1/matrix[j][i] and not matrix[i][j] == 1:
            flag = "Yes"
            break
        
print(flag)
