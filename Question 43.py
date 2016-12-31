import itertools
import time

start = time.time()

def pandigitals():
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    p = list(itertools.permutations(digits))
    return [''.join(x) for x in p if x[0] != '0']

def div_list(n):
    return [x for x in range(1000) if x % n == 0]

def div_lists():
    primes = [2, 3, 5, 7, 11, 13, 17]
    return [div_list(x) for x in primes]

d = div_lists()
l = pandigitals()

for loop in range(6, -1, -1):
    l = [x for x in l if int(x[loop+1:loop+4]) in d[loop]]
print(sum([int(x) for x in l]))

print(time.time() - start)

#16695334890