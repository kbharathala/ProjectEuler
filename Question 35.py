def flip(num):
    newstring = num
    i = 1
    while i < len(str(num)):
        newstring = str(newstring)[1:] + str(newstring)[0]
        if not is_prime(int(newstring)):
            return False
        i = i + 1
    return True

def test_list(nums):
    if not is_prime(nums):
        return False
    for i in range(0,len(str(nums)),1):
        if str(nums)[i] == 0:
            return False
    for i in range(0,len(str(nums)),1):
        if str(nums)[i] == 2:
            return False
    for i in range(0,len(str(nums)),1):
        if str(nums)[i] == 4:
            return False
    for i in range(0,len(str(nums)),1):
        if str(nums)[i] == 6:
            return False
    for i in range(0,len(str(nums)),1):
        if str(nums)[i] == 8:
            return False
    for i in range(0,len(str(nums)),1):
        if str(nums)[i] == 5:
            return False
    return True

def is_prime(num):
    if num == 2:
        return True
    for i in range(2,int(pow(num,.5)+1),1):
        if num % i == 0:
            return False
    return True


ans = 0
for each in range(1,1000000,1):
    if test_list(each):
        if flip(each):
            ans = ans + 1
            print(each)
print(ans)






