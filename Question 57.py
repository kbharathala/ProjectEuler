import time

def root(iterations):
    ans, num, denom = 0, 3, 2 #variables
    for n in range(0,iterations):
        num, denom = (num + 2 * denom), (num + denom)
        # a/b --> (a+2b) / (a+b) [next term]
        if len(str(num)) > len(str(denom)): #check if num has more digits
            ans += 1 
    return ans

def root_ans(iterations):
    num, denom = 3, 2 #variables
    for n in range(0,iterations):
        num, denom = (num + 2 * denom), (num + denom)
        # a/b --> (a+2b) / (a+b) [next term]
        print(str(num) + " / " + str(denom) + " " + str(num/denom))
    return

start = time.time()
print(root_ans(30))

print("time taken is  ",time.time() - start)
