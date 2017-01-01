def ways(int):
    a = 0
    num = 1
    sum = 0
    for i in range(0,int):
        num += a
        print(str(num) + " " + (str(i+1)))
        if i % 2 == 0:
            a = a *2
        if a == 0:
            a += 1
        sum += num
    return sum

print(ways(99))

# 1: 0
# 2: 1 (1, 1)
# 3: 2 (1, 1, 1), (1, 2)
# 4: 4 (1, 1, 1, 1), (1, 1, 2), (2, 2) (1, 3)
# 5: 6 (1 * 5), (1, 1, 1, 2), (1, 1, 3), (1, 4), (2, 3), (2, 2, 1)
# 6: f(5) + 

