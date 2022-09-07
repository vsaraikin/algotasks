n, m = 0, 2
line = [1, 3, 4]
first, second = [], []

def func(n, m):
    first.append(max(line[n], line[m]))
    second.append(min(line[n], line[m]))
    n += 1
    m -= 1
    if abs(m - n) in (0, 1):
        first.append(n)
        # print(first, second)
        return sum(first)
    else:
        func(n, m)
        
print(func(n, m))
