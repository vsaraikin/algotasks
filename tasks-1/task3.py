counter = 0
n = 1000

# output = 233168
for i in range(n):
    if (i % 3 == 0) or (i % 5 == 0):
        counter += i
        
print(counter)