n = 600851475143 # 1073676287

def check_if_prime(start, N):
    for i in range(start, int(pow(N, 0.5)) + 1):
        if N % i == 0:
            return False
    return True

num = n

l = []
def func(n):
    for i in range(2, num):
        if (n % i == 0):
            n = n / i
            if (check_if_prime(2, i) == True):
                l.append(i)
                print(l)
                return func(n)
            return func(n)
        if n == 1:
            return max(l)
        
print(func(n))            
