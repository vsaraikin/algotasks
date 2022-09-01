import itertools

# n = 10
# track_values = {
#     1: 1,
#     2: 2,
#     3: 3,
#     4: 4,
#     5: 5,
#     6: 6,
#     7: 7,
#     8: 8,
#     9: 9,
#     10: 10
# }

n = 6
track_values = {
    1: 1,
    2: 100,
    3: 3,
    4: 4,
    5: 1000,
    6: 0
}

# n = 2
# track_values = {
#     1: 8,
#     2: 9
# }

must_values = [1, list(track_values.values())[-1]]

# check for dummy values

if list(track_values.values())[-1] > n:
    print("-1")
    exit()

results_dict = {}  # key - list of position, values - res of mosquito


def res(count_2, count_3):
    return 2 * count_2 + 3 * count_3


def res_list(count_2, count_3):
    return [3] * count_3 + [2] * count_2


l = []

for l2 in range(int(n/2) + 1):
    for l3 in range(int(n/3) + 1):
        r = res(l2, l3)
        if r == n:
            l.append((l2, l3))


def generate_combination(numbers):
    results = set()
    for p in range(len(numbers), len(numbers) + 1):
        for x in itertools.permutations(numbers, p):  # n - length of each permutation
            results.add(int(''.join(map(str, x))))

    results = list(results)
    new_results = []
    for el in results:
        new_results.append([int(i) for i in str(el)])
    return new_results


all_combs = {}

for element in l:
    t1, t2 = element
    if t1 == 0 or t2 == 0:
        all_combs[(t1, t2)] = generate_combination(res_list(t1, t2))
        break
    else:
        all_combs[(t1, t2)] = generate_combination(res_list(t1, t2))


def get_mosquitoes_killed(track: dict, indexes: list):
    key = 1
    jumped_values = [key]
    for i in indexes:
        if key + i <= n:
            jumped_values.append(track[key + i])
            key += i
    last_element = list(track.keys())[-1]
    if last_element not in jumped_values:
        jumped_values.append(last_element)

    return jumped_values


for keys in all_combs:
    value = all_combs[keys]
    if len(value) <= 1:
        value = value[0] # fix
        tmp = get_mosquitoes_killed(track_values, value)
        results_dict[sum(tmp)] = tmp
    elif len(value) > 1:
        for element in value:
            tmp = get_mosquitoes_killed(track_values, element)
            results_dict[sum(tmp)] = tmp
    else:
        print('error')

print(results_dict[max(results_dict)])
