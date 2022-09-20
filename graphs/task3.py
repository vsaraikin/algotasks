n, m = 5, 4

input_lines = [
    [1, 2],
    [3, 4],
    [3, 2],
    [2, 4]
]

s = set()
    
s = {k:0 for k in range(1, n + 1)}

for pair in input_lines:
    s[pair[0]] += 1
    s[pair[1]] += 1

print(sorted(s.values(), reverse=True))
