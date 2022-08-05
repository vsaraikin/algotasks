n = 60081475143

# bruteforce slow

def check_if_prime(N):
    for i in range(2, N):
        if N % i == 0:
            return False
    return True

for i in range(2, n):
    if n % i == 0:
        if check_if_prime(i) == True:
            max_value = i
    
print(max_value)