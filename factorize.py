def factorize(num):
    list = []
    for i in range(1, int(pow(num,0.5)),1):
        if num % i == 0:
            list.append(int(i))
            list.append(int(num / i))
    return list

print(factorize(2013))
