import time
start = time.time()

def pentagonal(num):
    list = []
    for n in range(1,num+1):
        pent = int(((n*(3*n-1))/2))
        list.append(pent)
    return list

def checker(num,list):
    for n in range(0, len(list)):
        if num < list[n]:
            if num == list[n-1]:
                return True
            else:
                return False

pent = pentagonal(1000)
for int1 in pent:
    for int2 in pent:
        if int2 > int1:
            if checker(int(int1+int2),pent):
                print("Sum " + str(int1) + ", " + str(int2))
                if checker(int(int2-int1),pent):
                    print("Difference " + str(int1) + ", " + str(int2))

print (time.time() - start)
        
