counter = 0
n = 1000

# output = 233168
l1 = list(range(3, n+1, 3))
l2 = list(range(5, n, 5))
l3 = list(range(15, n, 15))      

print(sum(l1) + sum(l2) - sum(l3))
