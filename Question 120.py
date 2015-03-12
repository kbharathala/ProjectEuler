def method(a):
    max = 0
    x = 0
    for n in range(1,1000):
        value = (pow(a-1,n)+pow(a+1,n))%(pow(a,2))
        if value > max:
            max = value
            x = n
    return max

ans = 0
for n in range(3,1001):
    if n % 10 == 0:
        print(n)
    ans = ans + method(n)
print(ans)
    
        
