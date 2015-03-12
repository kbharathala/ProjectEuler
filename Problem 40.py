string = "0"
a = 1
while len(string) < 1000001:
    string = string + str(a)
    a = a + 1
print(string)
