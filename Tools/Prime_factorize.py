def is_prime(int):
    if int == 2:
        return True
    for i in range(2,int,1):
        if int % i == 0:
            return False
    return True

def prime_factorize(num):
    holder = num
    list = []
    while holder != 1:
        for i in range(2, int(pow(num,0.5)),1):
            if holder % i == 0 and is_prime(i):
                list.append(int(i))
                holder = holder/i
    return list

print(prime_factorize(123))
