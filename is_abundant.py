def factorize(num):
    list = [1]
    for i in range(2,1+int(pow(num,.5)) ,1):
        if num % i == 0:
            list.append(int(i))
            if int(num/i) != i:
                list.append(int(num/i))
    return list

def is_abundant(int):
    sum = 0
    for each in factorize(int):
        sum = sum + each
    if sum > int:
        return True
    else:
        return False

for each in range(1,10000,2):
    if is_abundant(each):
        print(each)

