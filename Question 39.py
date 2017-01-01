def triangle_creator(n):
    list = []
    for first in range(1,int(n/3+ 2)):
        for second in range(first+1, int(n/2 + 2)):
            third = n - first - second
            if third < first + second and first <= second and second <= third:
                list.append([first,second,third])
    return list
            
def pythag(n):
    hold = 0
    for each in triangle_creator(n):
        if pow(each[0], 2) + pow(each[1], 2) == pow(each[2],2):
            hold = hold + 1
    return hold

largest = 0
ans = 0
for num in range(4,1001,4):
    if num % 10 == 0:
        print(num)
    if pythag(num) > largest:
        largest = pythag(num)
        ans = num
print(largest,ans)
