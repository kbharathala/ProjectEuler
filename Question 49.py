import itertools

def prime(num):
    list = [2]
    for nums in range(3,num,2):
        a = 0
        for each in list:
            if nums % each == 0:
                a = 1
        if a == 0:
            list.append(nums)
    return list

def is_prime(num):
    if num == 2:
        return True
    for i in range(2,int(1+pow(num,.5)),1):
        if num % i == 0:
            return False
    return True

def num_to_list(num):
    list = []
    for each in str(num):
        list.append(int(each))
    return list

def get_permutations(num):
    total = []
    perms = list(itertools.permutations(num_to_list(num)))
    for each in perms:
        total.append(int(str(each[0])+str(each[1]) + str(each[2]) + str(each[3])))
    return list(set(total))

def get_clean_permutations(num):
    list = []
    for each in get_permutations(num):
        if is_prime(each) and each > 1000:
            list.append(each)
    return list

def check_arithmetic(prime):
    perms = get_clean_permutations(prime)
    num_dict = {}
    listt = []
    combs = list(itertools.combinations(perms, 2))
    for comb in combs:
        diff = abs(comb[1] - comb[0])
        if diff in num_dict:
            listt.append(comb[1])
            listt.append(comb[0])
            for each in num_dict[diff]:
                listt.append(each)
            return list(set(listt))
        else:
            num_dict[diff] = [comb[0], comb[1]]
    return []

primes = prime(10000)
i = 0
final = []

while i < len(primes):
    prime = primes[i]
    if prime < 1000:
        primes.remove(prime)
    else:
        clean_perms = get_clean_permutations(prime)
        for perm in clean_perms:
            if perm != prime or len(clean_perms) < 3:
                try:
                    primes.remove(perm)
                except:
                    pass
            else:
                final.append(prime)
                i = i + 1

for prime in final:
    ans = ''
    if(len(check_arithmetic(prime)) == 3):
        for each in check_arithmetic(prime):
            ans = ans + str(each)
        print(ans)
        
    





