def fact(n):
    a = 1
    for b in range(1,n+1):
        a = a * b
    return a

def choose(big,small):
    numerator = 1
    if big/2 > small:
        denominator = fact(small)
        small = big - small
    else:
        denominator = fact(big - small)
    for n in range(big,small,-1):
        numerator = numerator * n
    return int(numerator/denominator)
    
ans = 0
for first in range(1,101):
    for second in range(1,101):
        if choose(first,second) > 1000000:
            ans = ans + 1
print(ans)
