n = int(input())

d = {k:{} for k in range(1, n+1)}
for i in range(1, n+1):
    tmp = input().split()
    for x in range(1, 4):
        d[i][x] = int(tmp[x-1])

# Test

# n = 2
# d = {
#     1: {1:3, 2:4, 3:5},
#     2: {1:1, 2:1, 3:1},
# }


# n = 5
# d = {
#     1: {1:5, 2:10, 3:15},
#     2: {1:2, 2:10, 3:15},
#     3: {1:5, 2:5, 3:5},
#     4: {1:20, 2:20, 3:1},
#     5: {1:20, 2:1, 3:1},
#     }

iter_obj = iter(reversed(d.keys()))
ticket_list = []

for p in iter_obj:
    # compare lvl 1
    if p >= 3:
        tmp1, tmp2, tmp3 = d[p-2][3], d[p-1][2] + d[p-2][1], d[p-2][2] + d[p][1]
        ticket_list.append(min(tmp1, tmp2, tmp3))
        next(iter_obj)
        next(iter_obj)
        
    elif p == 2:
        tmp1, tmp2 = d[p-1][2], d[p-1][1] + d[p][1]
        ticket_list.append(min(tmp1, tmp2))
        next(iter_obj)

    elif p == 1:
        tmp1 = d[p][1]
        ticket_list.append(tmp1)
    else:
        print('error', p)
            
    
    # print(p, tmp1, tmp2, tmp3)

print(sum(ticket_list))
    
        