string = "0"
a = 1
while len(string) < 1000001:
    string = string + str(a)
    a = a + 1
ans = 1
for n in range(0,7,1):
    ans = ans * int(string[pow(10,n)])
print(str(ans))
    
