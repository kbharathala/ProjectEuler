def factorial(x):
    products = 1
    for nums in range(1,x+1,1):
        products = products * nums
    return products

for nums in range(10,999999,1):
    i = 0
    sum = 0
    while i < len(str(nums)):
        sum = factorial(int(str(nums)[i])) + sum
        i = i + 1
    if sum == nums:
        print(nums)

