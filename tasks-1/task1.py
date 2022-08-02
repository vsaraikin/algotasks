# input matrix
arr = [[3,3],
       [5, 3, 1],
       [5, 2, 5],
       [2, 5, 5]]


# output = 1

# if a[i][j] is on edge => skip
# elif a[i][j] has neighbors => find the min value => add to counter

true_list = [] # list which contains pits

for i in range(len(arr)):
    for j in range(len(arr[i])): 
        if (i == len(arr)-1) | (i == 0): # drop of upside and down rows
            break
        if (j != 0) & ((arr[i][j] == arr[i][-1]) == False): # drop of left and right columns
            pit = arr[i][j] # targeting at center
            
            up = arr[i-1][j]
            down = arr[i+1][j]
            left = arr[i][j-1]
            right = arr[i][j+1]
            
            min_neighboor = min(up, down, left, right)
            res = min_neighboor - arr[i][j]
            if res > 0:  
                true_list.append(res)
                
print(sum(true_list))