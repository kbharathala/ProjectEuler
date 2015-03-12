import time 

def is_prime(test):
    if test == 2:
        return True
    for i in range(2,int(pow(test,.5)),1):
        if test % i == 0:
            return False
    return True

def factorize(num):
    holder = num
    list = []
    while holder != 1:
        for i in range(2,holder+1):
            if is_prime(i):
                if holder%i == 0:
                    list.append(i)
                    holder = int(holder/i)
                    break
    return list

def num_dist_fact(num):
    return len(set(factorize(n)))

n = 192388

start = time.clock()
print(factorize(n))
elapsed = time.clock()

print(num_dist_fact(n))


elapsed = elapsed - start

print(elapsed)  
