def cycle(num):
    quotient = 1.0/num
    print(quotient)
    quotient = str(quotient)
    if len(quotient) < 10:
        return 0
    n = 2
    while quotient[n] == 0:
        n += 1
    first_dig = n
    first = quotient[n]
    a = 1
    while quotient[n+1] != first and a < 16:
        n += 1
        a += 1
    if a == 10:
        return False
    return n - first_dig + 1

for n in range(2,20):
    print(cycle(n))
