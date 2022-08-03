counter = 0
n = 1000

# output = 233168
l1 = range(3, n+1, 3)
l2 = range(5, n, 5)
l3 = range(15, n, 15)      

print(sum(l1) + sum(l2) - sum(l3))
