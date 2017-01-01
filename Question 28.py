import time
start = time.time()

increment, ans, num = 0, 1, 1
while increment < 1000 :
    increment += 2
    for n in xrange(4):
        num += increment
        ans += num
print(ans)

print(time.time() - start)

#669171001
