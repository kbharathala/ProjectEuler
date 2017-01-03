import copy
import time

start = time.time()

l = list(reversed([line.split() for line in open('p067_triangle.txt', 'r')]))

for i in xrange(1, len(l)):
	l[i] = [max(int(l[i-1][x]), int(l[i-1][x+1])) + int(l[i][x]) \
			for x in xrange(len(l[i]))]

print(l[-1])
print(time.time() - start)

# 7273


