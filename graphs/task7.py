n = 6

A = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

lines = []


for i in range(n):
    for j in range(n):
        if A[i][j] == 1:
            lines.append((i + 1, j + 1))

pairs_dict = {}
for pair in lines:
    if pairs_dict.get(pair[1]) is None:
        pairs_dict[pair[1]] = []
        pairs_dict[pair[1]].append(pair[0])
    else:
        pairs_dict[pair[1]].append(pair[0])


    
all_elements = {x for sub in lines for x in sub}
second_el = {pair[1] for pair in lines}
root = all_elements.difference(second_el).pop()

del second_el


for el in all_elements:
    if pairs_dict.get(el) is None:
        print(0, end='')
        
    else:
        print(pairs_dict.get(el)[0], end='')
    