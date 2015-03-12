def num_bubblesort(list):
    n = len(list)
    a = 1
    while a != 0:
        swapped = False
        for i in range(0,n-1,1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swapped = True
        if swapped == False:
            a = 0
    return list

pi = [101.4,1023.3, 12323, 123123, 423, 1.12, .111111, 101.3]
print(num_bubblesort(pi))
