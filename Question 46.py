def concatenate(string):
    decimal = string.find(".")
    return string[:decimal]

def is_prime(num):
    if num == 2:
        return True
    for i in range(2,num,1):
        if num % i == 0:
            return False
    return True

def goldbachs_conjecture(n):
    temp = 0
    square = 0
    while True:
        if is_prime(n):
            return False
        while pow(square,2) < (n/2):
            if is_prime(n - int(2*pow(square,2))):
                return False
            else:
                square += 1
        return True

for each in range(3,10001,2):
    if(goldbachs_conjecture(each)):
        print(str(each) + " is True!")

