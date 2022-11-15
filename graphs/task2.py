# n, m = [int(x) for x in input().split()]

# paths = []

# for _ in range(m):
#     paths.append([int(x) for x in input().split()])
    
    
n, m = 3, 3

input_lines = [
    [1, 2],
    [2, 3],
    [1, 2]
]

edges = {}
pairs_set = set()

# non-oriented graph: no loops and no multiple edges (verticles which connected 2+ times)
# mukltigraph:  no loops
# pseudograph: everything


loop = False
multilple_edges = False

for pair in input_lines:
    
    el1, el2 = pair[0], pair[1]
    
    if el1 == el2:
        loop = True
    
    if el2 > el1:
        pairs_set.add((el2, el1))
    else:
        pairs_set.add((el1, el2))

if len(pairs_set) == len(input_lines):
    multilple_edges = True
    

# non-oriented
if loop or multilple_edges:
    print('Yes')
else:
    print('No')

if not loop:
    print('Yes')
else:
    print('No')
    
print('Yes')
