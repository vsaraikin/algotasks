n, m = 5, 5

input_lines = [
    [1, 2],
    [3, 4],
    [1, 3],
    [3, 5],
    [1, 5]
]


n_lists = [[x] for x in range(1, n + 1)]


def check_if_merge(slice: list, el: int):
    for i in range(len(slice)):
        if el in slice[i]:
            return i
    
    return
        
    
for pair in input_lines:
    for i in range(n):
        if pair[0] in n_lists[i]:
            n_lists[i].append(pair[1])

            res = check_if_merge(n_lists[i:], pair[0])
            if res is not None and len(n_lists) > 1:
                n_lists[i] = n_lists[i] + n_lists[1 + i + res]

                n_lists.pop(1 + i + res)
            print(len(n_lists))
            break

        elif pair[1] in n_lists[i]:
            n_lists[i].append(pair[0])
            
            res = check_if_merge(n_lists[i:], pair[1])
            if res is not None and len(n_lists) > 1:
                n_lists[i] = n_lists[i] + n_lists[1 + i + res]

                n_lists.pop(1 + i + res)
            print(len(n_lists))
            break
        
        elif n_lists[i] == n_lists[-1]:
            n_lists.append(pair)
            print(len(n_lists))
            break
