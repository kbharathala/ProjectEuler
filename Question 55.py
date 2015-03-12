def is_palindrome(int):
    number = str(int)
    for i in range(0,len(number), 1):
        if number[i] != number[-i - 1]:
            return False
    return True

def reverse(number):
    num = str(number)
    new = ''
    for i in range(len(num)-1,-1,-1):
        new = new + num[i]
    ans = int(new)
    return ans

b = 0           
for i in range(1,10000,1):
    holder = i
    a = 1
    holder = holder + reverse(holder)
    while (a < 50):
        if is_palindrome(holder) == False:
            holder = holder + reverse(holder)
            a = a + 1
        else:
            b = b + 1
            a = 50
print(b)


