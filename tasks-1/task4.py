import random

# generate sequence
def generate_sequence() -> str:
    x = '0.'
    for i in range(1_000_001):
        yield str(i)


s = generate_sequence()

# generate list of indexes that you need to multiply
def generate_list() -> list:
    tmp = 1
    number_of_zeros = 6
    l_indexes = [tmp]

    for _ in range(number_of_zeros):
        tmp *= 10
        l_indexes.append(tmp)
    return l_indexes
        
        
list_indexes = generate_list()
print(list_indexes)
def res(s, list_indexes):
    location = 0
    res = 1
    for i in s:
        for x in i:
            if location in list_indexes:
                print(x)
                res *= int(x)
            location += 1
    return res
        

# Printing the result of the function res.
print(res(s, list_indexes))
