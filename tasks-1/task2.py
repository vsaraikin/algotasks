arr = [1, 3, 2, 5, 3, 4]

# out = [5, 5, 5, 0, 4, 0]

for i in range(len(arr)):
    m = max(arr[i:])
    if arr[i] < m:
        arr[i] = m
    else:
        arr[i] = 0
        
print(arr)
