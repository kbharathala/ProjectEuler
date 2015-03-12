def units(num):
    if num == 1:
        return 3
    if num == 2:
        return 3
    if num == 3:
        return 5
    if num == 4:
        return 4
    if num == 5:
        return 4
    if num == 6:
        return 3
    if num == 7:
        return 5
    if num == 8:
        return 5
    if num == 9:
        return 4
    if num == 0:
        return 0

def tens(num):
    if num == 2:
        return 6
    if num == 3:
        return 6
    if num == 4:
        return 5
    if num == 5:
        return 5
    if num == 6:
        return 5
    if num == 7:
        return 7
    if num == 8:
        return 6
    if num == 9:
        return 6
    if num == 0:
        return 0

def hundreds(num):
    if num == 1:
        return 13
    if num == 2:
        return 13
    if num == 3:
        return 15
    if num == 4:
        return 14
    if num == 5:
        return 14
    if num == 6:
        return 13
    if num == 7:
        return 15
    if num == 8:
        return 15
    if num == 9:
        return 14

ans = 0
for each in range(1,10,1):
    ans = ans + units(each)
print(ans)

for each in range(10,100,1):
    if int(str(each)[0]) == 1:
        if each == 10:
            ans = ans + 3
        if each == 11:
            ans = ans + 6
        if each == 12:
            ans = ans + 6
        if each == 13:
            ans = ans + 8
        if each == 14:
            ans = ans + 8
        if each == 15:
            ans = ans + 7
        if each == 16:
            ans = ans + 7
        if each == 17:
            ans = ans + 9
        if each == 18:
            ans = ans + 9
        if each == 19:
            ans = ans + 8
    else:
        ans = ans + tens(int(str(each)[0])) + units(int(str(each)[1]))
        
print(ans)

for each in range(100,1000,1):
    ans = ans + hundreds(int(str(each)[0]))
    other = str(each)[1:]
    if int(str(each)[1]) == 1:
        if other == 10:
            ans = ans + 3
        if other == 11:
            ans = ans + 6
        if other == 12:
            ans = ans + 6
        if other == 13:
            ans = ans + 8
        if other == 14:
            ans = ans + 8
        if other == 15:
            ans = ans + 7
        if other == 16:
            ans = ans + 7
        if other == 17:
            ans = ans + 9
        if other == 18:
            ans = ans + 9
        if other == 19:
            ans = ans + 8
    else:
        ans = ans + tens(int(str(each)[1])) + units(int(str(each)[2])) 
    
print(ans)
