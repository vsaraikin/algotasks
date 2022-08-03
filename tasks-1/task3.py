counter = 0
n = 1000

# output = 233168
l1 = set(range(3, n+1, 3))
l2 = set(range(5, n, 5))
print(sum(set.union(l1, l2)))
        

# counter = sum([i for i in range(n) if (i % 3 == 0) or (i % 5 == 0)])
# print(counter)