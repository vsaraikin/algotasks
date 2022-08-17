import itertools
start = 1
end = 31
soliders = [i for i in range(start, end + 1)]


def even_list(last: int):
    numbers = range(1, last + 1)
    return len([x for x in numbers if not (x & 1)])

def odd_list(last: int):
    numbers = range(1, last + 1)
    return len([x for x in numbers if x & 1])

def generate_pair(n):
    """ 0 - odd, 1 - even"""
    pairs = []
    for i in range(0, n + 1):
        odd, even = (i, n - i)
        pairs.append([0] * odd + even * [1])
    return pairs

def division_number(soliders: list):
    c = 0
    while len(soliders) >= 3:
        soliders = soliders[int(len(soliders)/2):]
        c += 1
    return c

generate_pairs = generate_pair(division_number(soliders))


def generate_combination(default: list) -> set:
    """ Returns set of possible combinations """
    combinations = {tuple(map(int, x)) for x in itertools.permutations("".join(map(str, default)))}
    return combinations


all_possible_combinations = [generate_combination(x) for x in generate_pairs]

def divide_until_res(elements: list) -> bool:
    """ Divide by even or odd element until the length of array == 2 or == 3"""
    res = len(soliders)
    number_of_actions = 0
    i = 0
    l = []
    while res > 3:
        var = elements[i]
        l.append(elements[i])
        i += 1
        number_of_actions += 1
        if var == 0:
            res = even_list(res)
        elif var == 1:
            res = odd_list(res)
        else:
            print('error')

    return res, l


s = set()
for sub in all_possible_combinations:
    for combination in sub:
        tmp = divide_until_res(combination)
        if tmp[0] < 4:
            s.add(tuple(tmp[1]))
            
print(len(s))