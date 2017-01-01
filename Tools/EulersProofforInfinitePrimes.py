def prime(num):
    list = []
    list.append(2)
    product = 2
    for nums in range(3,num,1):
        a = 0
        for each in list:
            if nums % each == 0:
                a = 1
        if a == 0:
            list.append(nums)
            print(nums)
            product = nums * product
    return product

def is_prime(int):
    if int == 2:
        return True
    for i in range(2,int,1):
        if int % i == 0:
            return False
    return True

print(prime(20) + 1)
print(is_prime(prime(20) + 1))
        
