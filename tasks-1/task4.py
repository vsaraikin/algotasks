import random

# generate sequence
def generate_sequence() -> str:
    x = '0.'
    for _ in range(1000000):
        x += str(random.randint(1, 100000))
    return x

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

def res(s, list_indexes):
    s = s[1:] # remove dot and zero
    res = 1
    for i in range(1, len(s)):
        if i in list_indexes:
            print(s[i])
            res *= int(s[i])
        
    return res

print(res(s, list_indexes))
