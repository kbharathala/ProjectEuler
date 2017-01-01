from collections import Counter
import time

start = time.time()

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

def totient(n):
    return len([x for x in range(n) if gcd(n, x) == 1])

# def score(n):
#     return float(n)/totient(n)

def is_permutation(a, b):
    if len(str(a)) != len(str(b)):
        return False
    return Counter(list(str(b))) == Counter(list(str(a)))

l = []
for x in xrange(2, 2000):
    t = totient(x)
    if is_permutation(x, t):
        l.append((float(x) / t, t, x))

print(l)

print(time.time() - start)
