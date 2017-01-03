import time
start = time.time()

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(2,int(1+pow(num,.5)),1):
        if num % i == 0:
            return False
    return True

def prime_list(num):
    return [x for x in xrange(num) if is_prime(x)]

MAX_VAL = 50000000

# Roughly 7k
p = prime_list(int(MAX_VAL ** 0.5))
l = set([])

for i in p:
    for j in p:
        temp = i ** 2 + j ** 3
        if temp > MAX_VAL:
            break
        for k in p:
            curr = temp + k ** 4
            if curr > MAX_VAL:
                break
            l.add(curr)

print(len(l))
print(time.time() - start)

# 1097343