line = [1, 3, 4, 1, 2]
n, m = 0, len(line) - 1


first, second = [], []

def func(n, m):
    first.append(max(line[n], line[m]))
    second.append(min(line[n + 1], line[m - 1]))
    
    n += 1
    m -= 1
    
    if abs(m - n) == 0:
        first.append(min(line[n + 1], line[n]))
        
        # print(first, second)
    elif abs(m - n) == 1:
        first.append(max(line[n + 1], line[n]))
        second.append(min(line[n + 1], line[n]))
        # print(first, second)
    else:
        func(n, m)
        
func(n, m)
print(sum(first))
