import time
start = time.time()

# def gcd(x, y):
#     return x if y == 0 else gcd(y, x % y)

# def score(n):
#     return float(n) / len([x for x in range(n) if gcd(n, x) == 1])

# p1 = prime_list(10000)
# l = [x for x in range(2, 10000) if x not in p1 or x / 2 not in p1 or x / 3 not in p1]

# max, max_index = 0, 0
# for x in l:
#     s = score(x)
#     if s > max:
#         max, max_index = s, x

# print(max, max_index)

def is_prime(n):
    if n == 2 or n == 3:
        return True
    for i in range(2,int(n**.5)+1):
        if n % i == 0:
            return False
    return True

def prime_list(n):
    return [x for x in range(2, n) if is_prime(x)]

p = prime_list(100)

prod = 1
i = 0
while prod < 1000000:
    prod *= p[i]
    i += 1
print(prod / p[i-1])

print(time.time() - start)
