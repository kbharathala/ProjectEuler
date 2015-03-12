import time
start = time.time()

def pentagonal(n):
    return(int(((n*(3*n-1))/2)))

def checker(num,list):
    for n in range(0, len(list)):
        if num > list[n]:
            if num == list[n-1]:
                return True
            else:
                return False
size = 1000
pent = []
for each in range(1,size):
    pent.append(pentagonal(each))
for n in range(1,size,1):
    for num in range(0,size-n-1):
        if checker((pent[num]+pent[num+n]),pent):
            print(pent[num],pent[num+n])
            if checker((pent[num+n]-pent[num]),pent):
                print("YEHSEYHSYEHSYEHSYEHSYESHEY" + str((pent[num+n]-pent[num])))

print (time.time() - start)
        
