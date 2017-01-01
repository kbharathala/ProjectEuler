from collections import Counter
import time
start = time.time()

d = {}
i = 1

while True:
	# Stores the counter in a usable format for the hash
	# "((2, 2), (3, 2), (4, 1))"
	k = str(dict(Counter(list(str(i ** 3)))).items())
	if k in d:
		d[k].append(i ** 3)
		if len(d[k]) == 5:
			print(d[k][0])
			break
	else:
		d[k] = [i ** 3]
	i += 1

print(time.time() - start)



