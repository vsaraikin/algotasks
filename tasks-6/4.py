import copy

n = int(input())
nails = [int(input()) for _ in range(n)]

# Test

# n = 5
# nails = [11, 12, 13, 16, 17]

# n = 4
# nails = [6.34, 6.82, 15.89, 24.58]

nails_copy = copy.deepcopy(nails)
visited = set()

def foo(nails_list: list):
    
    s = 0
    
    for el in nails_list:
        if el not in visited:
            results = sorted([(nails_list[x+1] - nails_list[x], (nails_list[x], nails_list[x+1])) for x in range(len(nails_list)-1)])
            print(results)
            pair = results[0][1]
                        
            visited.add(pair[0])
            visited.add(pair[1])
            
            s += abs(pair[1] - pair[0])
            
            nails_list.remove(pair[0])
            nails_list.remove(pair[1])
        
        if len(nails_list) == 1:
            el = nails_list[0]
            final_el = sorted([(abs(x-el), x) for x in nails_copy])[1][1]
            s += abs(el-final_el)
            
            visited.add(el)
            nails_list.remove(el)
            
    return s.__round__(3)

            
print(foo(nails))