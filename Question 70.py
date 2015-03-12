def is_prime(num):
    if num == 2:
        return True
    for i in range(2,int(pow(num,.5)+1),1):
        if num % i == 0:
            return False
    return True

def rel_prime(a,b): # a < b
    if is_prime(a) and b%a != 0:
        return True
    if is_prime(b):
        return True
    for num in range(2,a+1):
        if a % num == 0 and b % num == 0:
            return False
    return True

def totient(n):
    ans = 0
    for num in range(2,n):
        if num % 100 == 0:
            print(num)
        if rel_prime(num,n):
            ans += 1
    return ans

print(totient(87109))
