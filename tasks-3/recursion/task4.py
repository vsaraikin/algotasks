line = [3, 3, 3, 0, 1, 1, 1]
n, m = 0, len(line) - 1


first, second = [], []

def func(n, m):
    first.append(max(line[n], line[m]))
    second.append(min(line[n], line[m]))
    
    n += 1
    m -= 1
    
    if abs(m - n) == 1:
        first.append(max(line[n], line[m]))
        second.append(min(line[n], line[m]))
        print(1)
    elif abs(m - n) == 0:
        first.append(line[n])
        print(0)

    else:
        func(n, m)
        
func(n, m)
print(first, second)
