def prime(num):
    list = [2]
    for nums in range(3,num,2):
        a = 0
        if nums % 100 == 1:
            print(nums)
        for each in list:
            if nums % each == 0:
                a = 1
        if a == 0:
            list.append(nums)
    return list

