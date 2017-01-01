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

print(is_pandigital(123456789,9))
print(is_pandigital(987654321,9))
print(is_pandigital(1231385742,9))
print(is_pandigital(3124,4))
