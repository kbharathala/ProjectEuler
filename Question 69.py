def is_prime(num):
    if num == 2:
        return True
    for i in range(2,int(1+pow(num,.5)),1):
        if num % i == 0:
            return False
    return True

def totient(num):
    list = []
    temp = []
    for each in range(2,num):
        list.append(each)
        temp.append(each)
    for each in list:
        if is_prime(each):
            if num % each == 0:
                index = temp.index(each)
                temp.pop(index)
                for all in range(2,int(num/each)):
                    index = temp.index(all*each)
                    temp.pop(index)
    return num / (len(temp)+1), num

max = 0
for num in range(2,101):
    print(totient(num))
