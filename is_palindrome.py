def is_palindrome(int):
    number = str(int)
    for i in range(0,len(number), 1):
        if number[i] != number[-i - 1]:
            return False
    return True
            
