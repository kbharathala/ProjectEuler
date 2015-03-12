def is_prime(int):
    if int == 1:
        return False
    if int == 2:
        return True
    for i in range(2,int,1):
        if int % i == 0:
            return False
    return True

def prime(num):
    list = []
    list.append(2)
    for nums in range(3,num,1):
        a = 0
        for each in list:
            if nums % each == 0:
                a = 1
        if a == 0:
            list.append(nums)
    return list

ans = 0
sum = 0
i = 11
list = []
ans_list = []
for i in prime(200000):
    holder = i
    num = i
    while (True):
        if is_prime(holder):
            if len(str(holder)) == 1:
                list.append(i)
                ans = ans + 1
                break
            else:
                holder = int(str(holder)[1:])        
        else:
            break
    if i % 1000 == 0:
        print(i)
        print(len(list))
    i = i + 1

for num in list:
    holder = num
    while(True):
        if is_prime(holder):
            if len(str(holder)) == 1:
                ans_list.append(num)
                ans = ans + 1
                break
            else:
                holder = int(str(holder)[:-1])
        else:
            break

print(ans_list)

    
