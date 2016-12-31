import time
start = time.clock()

def is_prime(n):
    if n == 2 or n == 3:
        return True
    for i in range(2,int(n**.5)+1):
        if n % i == 0:
            return False
    return True

def prime_list():
    return [x for x in range(2, 1000) if is_prime(x)]

def num_dist_fact(num, p):
    return len([prime for prime in p if num % prime == 0])

p = prime_list()
n = 0

while(True):
    if num_dist_fact(n, p) == 4 and \
       num_dist_fact(n+1, p) == 4 and \
       num_dist_fact(n+2, p) == 4 and \
       num_dist_fact(n+3, p) == 4:
        print(n)
        break
    n += 1

elapsed = time.clock() - start
print(elapsed)
