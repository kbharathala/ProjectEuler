def bouncy(int):
    num = str(int)
    current = num[0]
    increase = False
    decrease = False
    for i in range(1,len(num),1):
        next = num[i]
        if next != current:
            if next > current:
                if decrease == True:
                    return True
                else:
                    increase = True
            else:
                if increase == True:
                    return True
                else:
                    decrease = True
        current = next
    return False

a = 0
n = 2000000
while(100*a < 99*i):
for i in range(0,n,1):
    if bouncy(i):
        a = a + 1
print(a/n)
