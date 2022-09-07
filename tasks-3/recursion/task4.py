line = [2, 3, 100, 10, 1, 3]
n, m = 0, len(line) - 1


first, second = [], []

def func(n, m):
    if line.index(max(line[n + 1], line[m - 1])) - n == 1:
        first.append(line[m])
        second.append(line[n])
    else:
        first.append(line[m])
        second.append(line[n])
    
    
    n += 1
    m -= 1
    
    if abs(m - n) == 0:
        first.append(min(line[n + 1], line[n]))
        
        print(first, second)
    elif abs(m - n) == 1:
        first.append(max(line[n], line[n + 1]))
        second.append(min(line[n], line[n + 1]))
        print(first, second)
    else:
        func(n, m)
        
func(n, m)
print(first)
