def is_prime(int):
    if int == 2:
        return True
    for i in range(2,int,1):
        if int % i == 0:
            return False
    return True

ans = 0
for num in range(1,100,1):
    a = 1
    while a != 0:
        for n in range(1,len(str(list)) + 1,1):
            loop = str(num)[-n] + str(num)[:len(str(list))-1]
            if not is_prime(int(loop)):
                a = 0
                break
        print(num)
        ans = ans + 1
print(ans)
        
    
        
    
