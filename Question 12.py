def factorize(num):
	list = []
	i = 1
	while i <= pow(num,.5):
		if num % i == 0:
			list.append(i)
			list.append(num/i)
		i = i + 1
	return len(list)
    
def triangle(num):
	return ((num)*(num + 1)/2)
for i in range(10000,15000,1):
	if factorize(triangle(i)) > 500:
		print(triangle(i))
