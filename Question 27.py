def is_prime(int):
    if int == 2:
        return True
    for i in range(2,int,1):
        if int % i == 0:
            return False
    return True

def formula(a,b):
    len = 0
    while True:
        for n in range(0,80):
            ans = pow(n,2) + a*n + b
            if not is_prime(abs(ans)):
                return len
                break
            else:
                len = len + 1
        return len
final = 0
for a in range(-100,1000):
    if a % 10 == 0:
        print(a)
    for b in range(-999,1000):
        if formula(a,b) > final:
            final = formula(a,b)
            print(final)
            print (a,b)

    

