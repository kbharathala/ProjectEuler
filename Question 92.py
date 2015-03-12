def squaredigit(num):
    ans = num
    while True:
        hold = 0
        for each in str(ans):
            hold = hold + pow(int(each),2)
        ans = hold
        #print(ans)
        if ans == 1:
            ans = 0
            return False
        if ans == 89:
            ans = 0
            return True

b = 0
for all in range(1,10000001,1):
    if all % 1000 == 0:
        print(all)
        print(b)
    if squaredigit(all):
        b = b + 1
print(b)
        
