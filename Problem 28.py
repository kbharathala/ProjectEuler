def divisors(n):
   list = [1]
   for num in range(2,int(pow(n,.5)+ 1)):
       if n % num == 0:
           if pow(num,2) != n:
               list.append(int(n/num))
           list.append(int(num))         
   return(list)

def div_sum(n):
   sum = 0
   for each in divisors(n):
       sum = sum + each
   return sum

def amicable(n):
   hold = div_sum(n)
   list = [hold]
   a = 0
   while hold != n and a < 30:
       hold = div_sum(hold)
       if hold > 1000000:
           return False
       list.append(hold)
       a = a + 1
       #print(hold)
   if hold == n:
       return len(list)
   else:
       return 0

largest = 0
for each in range(1,1000000):
   if each % 1000 == 0:
       print(each)
   if amicable(each) > largest:
       largest = amicable(each)
print(largest)
 
