def digitsum(num):
    string = str(num)
    sum = 0
    for i in range(0,len(string),1):
        sum = sum + int(string[i])
    return sum
max = 0
for a in range(1,100,1):
    for b in range(1,100,1):
        if digitsum(a ** b) > max:
            max = digitsum(a ** b)
print(max)
