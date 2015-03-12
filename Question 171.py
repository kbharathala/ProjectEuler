def is_square(num):
    sqrt = int(pow(num,.5))
    if sqrt*sqrt < num:
        return False
    else:
        return True

def sum_squares(num):
    string = str(num)
    sum = 0
    for each in string:
        sum = sum + pow(int(each),2)
    return sum

def function(num):
    return is_square(sum_squares(num))

sum = 0
for each in range(1,10000000):
    if function(each):
        sum = sum + each
print(sum)
