from itertools import chain


counter = 0
n = 1000

# output = 233168
l1 = list(range(3, n+1, 3))
l2 = list(range(5, n, 5))
      
l3  = l1 + l2

def unique(n):
    u_list = []
    for i in n:
        if i not in u_list:
            u_list.append(i)
    return u_list


print(sum(unique(l3)))
