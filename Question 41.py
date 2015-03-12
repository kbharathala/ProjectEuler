def is_pandigital(num,n):
    test_case = []
    list = []
    string = str(num)
    for all in range(1,n+1):
        test_case.append(all)
    for each in string:
        list.append(int(each))
    list.sort()
    if list == test_case:
        return True
    return False

def is_prime(num):
    if num == 2:
        return True
    for i in range(2,int(1+pow(num,.5)),1):
        if num % i == 0:
            return False
    return True

largest = 0
for second in range(2,9):
    for first in range(pow(10,second-1),pow(10,second)):
        if is_pandigital(first,second):
            if is_prime(first):
                if first > largest:
                    largest = first
print(largest)
    
