import math

possible_pairs = []

n = 5

for long_multiplier in range(n):
    short = n - long_multiplier * 2
    if short < 0:
        break
    # print(f"Short + Long * 2: {short} + {long_multiplier} * 2 = {short + long_multiplier * 2}")
    possible_pairs.append((short, long_multiplier))


res = 0
for pair in possible_pairs:
    res += math.comb(sum(pair), max(pair))

print(res)
