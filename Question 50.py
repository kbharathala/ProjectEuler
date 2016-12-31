import time
start = time.time()

def is_prime(n):
    if n == 2 or n == 3:
        return True
    for i in range(2,int(n**.5)+1):
        if n % i == 0:
            return False
    return True

def prime_list(n):
    return [x for x in range(2, n) if is_prime(x)]

p1 = prime_list(1000000)
p2 = prime_list(50000)

max_len = len(p2)
print(max_len)

# 21 because that was the length of the previous longest
for l in range(21, max_len):
	for j in range(max_len - l):
		curr = sum(p2[j:j+l])
		if curr in p1:
			print l, curr
			break
		if curr > 1000000:
			break

print(time.time() - start)

## 997651 --> length 543