import time
start = time.time()

def pentagonal(n):
    list = []
    for num in range(1,n+1):
        list.append((n*(3*n-1))/2)
    return list

def sum_list(list):
    sum = []
    for int1 in list:
        for int2 in list:
            if int1 < int2:
                sum.append(int1+int2)
    return sum

def diff_list(list):
    diff = []
    for int1 in list:
        for int2 in list:
            if int1 < int2:
                diff.append(int2-int1)
    return diff

ans = 0
pentag = pentagonal(1000)
pent = set(sum_list(pentag))
pent.sorted()
for each in sum_list:
    if each[0] in pentag:
        if each[1] in pentag:
            print(each)
print(ans)
print (time.time() - start)
        
