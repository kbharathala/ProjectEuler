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

def test(num1,num2):
    string = str(num1)+str(num2)+str(num1*num2)
    if len(string) < 9:
        return False
    if is_pandigital(int(string),9):
        return True
    return False

final = []
ans = 0
for num1 in range(1,100):
    if num1 % 5 == 0:
        print(num1)
    for num2 in range(num1,10000):
        if test(num1,num2):
            final.append(num1*num2)
final = list(set(final))
for each in final:
    ans += each
print(ans)
