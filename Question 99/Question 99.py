import time
import math

start = time.time()

f = open('p099_base_exp.txt', 'r')

max, index = 0, 0
for i, line in enumerate(f.readlines()):
	l = line.split(',')
	val = int(l[1]) * math.log(float(l[0]))
	if val > max:
		max, index = val, i

print(index+1)
print(time.time() - start)

# 709