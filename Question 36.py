def is_palindrome(int):
    number = str(int)
    for i in range(0,len(number), 1):
        if number[i] != number[-i - 1]:
            return False
    return True
            
sum = 0
for i in range(1,1000000,1):
    if is_palindrome(i):
        binary = int(bin(i)[2:])
        if is_palindrome(binary):
            sum = sum + i
print(sum)
