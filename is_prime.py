def is_prime(num):
    if num == 2:
        return True
    for i in range(2,int(1+pow(num,.5)),1):
        if num % i == 0:
            return False
    return True

for i in range (2, 50, 1):
    print(str(i) + ' ' + str(is_prime(i)))
