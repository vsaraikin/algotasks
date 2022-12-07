n = 6

def max_level(n):
    
    s = 0
    for i in range(1, n):
        s += i

        if s == n:
            return i
        
        elif s > n:
            return i - 1
        

# Generate ladder
def generate_ladder_dict(n):
    
    current_bricks = 0
    
    max_l = max_level(n)
    d = {}
    for levl in range(max_l, 0, -1):
        
        current_bricks += 1
        d[levl] = current_bricks
        
    
    if n - sum(d.values()) != 0:
        for levl in range(1, max_l + 1):
            
            d[levl] += 1
            
            if n - sum(d.values()) == 0:
                break

    return d

d = generate_ladder_dict(n)

def find_following_minimum(d):
    fm = max(d.keys())
    
    dm2 = d.get(fm - 2)
    dm1 = d.get(fm - 1)
    
    if dm2 != None and dm1 != None:
        if dm2 - dm1 > 1:
            return fm - 1
        else:
            return min(d.keys())
    else:
        return min(d.keys())
        
        
# Non-recursive solution
# def count(ladders_dict):
#     ways = 0

#     for _ in range(n):
#         # d[3]  # move to lowest level
#         cur_max = max(ladders_dict.keys())
#         cur_min = find_following_minimum(ladders_dict)
        
#         if cur_max == cur_min:
#             break
        
#         ladders_dict[cur_max] -= 1
#         ladders_dict[cur_min] += 1
        
#         if ladders_dict[cur_max] == 0:
#             ladders_dict.pop(cur_max)
        
#         ways += 1
         
#     return ways + 1


# Recursive solution
def count_rec(ladders_dict, ways):
    cur_max = max(ladders_dict.keys())
    cur_min = find_following_minimum(ladders_dict)
    
    if cur_max == cur_min:
        return ways + 1
    else:
        ladders_dict[cur_max] -= 1
        ladders_dict[cur_min] += 1
        
        if ladders_dict[cur_max] == 0:
            ladders_dict.pop(cur_max)
        
        ways += 1
        return count_rec(ladders_dict, ways)

# print(count(d))
print(count_rec(d, 0))