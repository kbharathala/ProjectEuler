import time 

start = time.clock()

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
    return len(set(factorize(num)))

for n in range(12000,100000):
    if n%100 == 0:
        print(n,"haha")
    if(num_dist_fact(n))==4 and (num_dist_fact(n+1))==4 and (num_dist_fact(n+2))==4:
        print(n)

elapsed = time.clock()
elapsed = elapsed - start

print(elapsed)
