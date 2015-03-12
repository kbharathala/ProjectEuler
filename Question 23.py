import time
start = time.time()

def factorize(num):
    list = [1]
    for i in range(2,1+int(pow(num,.5)) ,1):
        if num % i == 0:
            list.append(int(i))
            if int(num/i) != i:
                list.append(int(num/i))
    return list

def abundant(int):
    sum = 0
    for each in factorize(int):
        sum = sum + each
    if sum > int:
        return True
    else:
        return False

def abundant_list(int):
    list = []
    for each in range(1,int):
        if abundant(each):
            list.append(each)
    return list

def sum_list(list):
    sum = []
    for int1 in list:
        for int2 in list:
            if int1 + int2 < 28123:
                sum.append((int1 + int2))
    return sum

ans = 0
sum = sorted(set(sum_list(abundant_list(28123))))
for num in range(1,28123):
    if num not in sum:
        ans += num
print(ans)
print (time.time() - start)
