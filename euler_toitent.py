def totient(num):
    list = []
    for i in range(1,num,1):
        if num % i != 0:
            list.append(i)
    return list

print(totient(5))
