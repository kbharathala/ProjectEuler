for each in range(9123,9876):
    test_case = []
    for all in range(1,10):
        test_case.append(all)
    h=str(each)+str(each*2)
    i=[]
    for each in h:
        i.append(int(each))
    i.sort()
    if i==test_case:
        print (h)
