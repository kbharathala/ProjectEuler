import time

start = time.time()

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

def is_prime(num):
    if num == 2:
        return True
    for i in range(2,int(1+pow(num,.5)),1):
        if num % i == 0:
            return False
    return True

MAX_NUM = 10000
count = 0

for i in xrange(MAX_NUM, 5, -1):
	if is_prime(i):
		count += (MAX_NUM - i)
	else:
		for j in xrange(2, i):
			if gcd(i, j) != 1:
				count += 1

print((MAX_NUM ** 2 - MAX_NUM) / 2 - count)







print(time.time() - start)