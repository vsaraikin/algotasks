# line = [1, 3, 4]
line = [1, 3, 4, 1, 2]

n, m = 0, -1


first, second = [], []

def func(n, m):
    tmp_first_max = max(line[n], line[m])
    first.append(tmp_first_max)
    line.remove(tmp_first_max)
    
    tmp_second_max = max(line[n], line[m])
    second.append(tmp_second_max)
    line.remove(tmp_second_max)
    
    
    if len(line) == 1:
        first.append(line[n])
        print(first, second)
        
    elif len(line) == 2:
        first.append(max(line[n], line[m]))
        second.append(min(line[n], line[m]))
        print(first, second)
        
    else:
        func(n, m)
        
func(n, m)
print(sum(first))
