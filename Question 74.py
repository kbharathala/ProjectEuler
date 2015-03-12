import time
factorial = [1,1,2,6,24,120,720,5040,40320,362880]

def fact_sum(num):
    sum = 0
    for digit in str(num):
        sum = sum + factorial[int(digit)]
    return sum

start = time.time()
a = 0
for n in range(1,10000):
    if n % 100 == 0:
        print(n)
    holder = n
    list = [n]
    while fact_sum(holder) not in list:
        list.append(fact_sum(holder))
        holder = fact_sum(holder)
    else:
        if len(list) == 60:
            a += 1
print(a)
    
end = time.time() - start
print ('It took %f seconds.' % end)
