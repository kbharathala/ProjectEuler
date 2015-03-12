
increment = 0
ans = 1
num = 1
for time in range(0,500):
    increment = increment + 2
    if time % 10 ==0:
        print(time)
    for n in range(0,4):
        num = num + increment
        ans = ans + num
   
print(ans)
