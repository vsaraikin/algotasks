def first_divisor(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i

def get_radical(n):
    l = {first_divisor(n)}
    def radicalize(n):
        for i in range(max(l), 100000): 
            if n % i == 0:
                l.add(i)
                n = n / i 
                break
        if n == 1:
            return l
        else:
            return radicalize(n)
    res = radicalize(n)
    product = 1

    for item in res:
        product = product * item
    
    return product

def generate_radical_series(N):
    radicals_store = {}
    for i in range(2, N + 1):
        radicals_store[i] = get_radical(i)
        
    radicals_store = {k: v for k, v in sorted(radicals_store.items(), key=lambda item: item[1])}
    return radicals_store

def get_K_value(K, N):
    store = generate_radical_series(N)
    return list(store.keys())[K-2]

N = 10000
K = 10000
print(get_K_value(K, N))