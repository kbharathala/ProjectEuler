import time

start = time.time()
 
n = 2
for i in xrange(7830456):
    n = (2 * n) % 10000000000
 
print((n * 28433 + 1) % 10000000000)

print(time.time() - start)