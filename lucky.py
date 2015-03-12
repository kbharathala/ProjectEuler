a = 0
for num in range(100,10000,1):
    string = str(num)
    if len(string) == 3:
        if int(string[0]) == int(string[1]) + int(string[2]):
            a = a + 1
    if len(string) == 4:
        if int(string[0]) + int(string[1]) == int(string[2]) + int(string[3]):
            a = a + 1
print(a)
