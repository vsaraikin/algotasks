n = 6

lines = [
    (3, 2),
    (5, 4),
    (3, 1),
    (3, 5),
    (5, 6)
]


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
    