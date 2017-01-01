def prime(num):
    list = []
    list.append(2)
    for nums in range(3,num,1):
        a = 0
        for each in list:
            if nums % each == 0:
                a = 1
        if a == 0:
            list.append(nums)
    return list

prime(100000).index(739397)
