import time
start = time.time()

def pentagonal(n):
    return(int(((n*(3*n-1))/2)))

size = 3000
pent = []

for i in range(1,size):
    pent.append(pentagonal(i))

for n in range(1,size):
    print(n)
    for num in range(0,size-n-1):
        if (pent[num]+pent[num+n] in pent):
            #print(pent[num],pent[num+n])
            if (pent[num+n]-pent[num] in pent):
                print(pent[num+n]-pent[num])

print (time.time() - start)