from math import floor
import time

start = time.time()

MAX_NUM = 1000000

l = [(floor(float(3)/7 * x) / x, x) for x in range(3, MAX_NUM+1)]
l.sort()

index = l.index((float(3)/7, 7)) - 1
print(int(l[index][0] * l[index][1]))

print(time.time() - start)

# 428570