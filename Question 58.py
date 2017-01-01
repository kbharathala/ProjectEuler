import time
start = time.time()

def is_prime(n):
    if n == 2 or n == 3:
        return True
    for i in range(2,int(n**.5)+1):
        if n % i == 0:
            return False
    return True

side = 3
primes = 0
total = 1
curr = 1

while True:
	total += 4
	for i in range(4):
		# Testing whether the four corners are prime
		curr += side - 1
		if is_prime(curr):
			primes += 1
	# "total" could be replaced with "2 * side - 1"; 
	# But this actually slows it down a little bit.
	if float(primes) / total < 0.1:
		break
	side += 2

print(side)
print(time.time() - start)
#26241
