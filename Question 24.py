def fact(num):
    ans = 1
    for n in range(num,1,-1):
        ans = ans * n
    return ans

def perm(number):
    list = [0,1,2,3,4,5,6,7,8,9]
    ans = []
    hold = number
    for n in range(9,-1,-1):
        residue = int(hold/fact(n))
        #print(residue)
        ans.append(list[residue])
        list.pop(residue)
        hold = hold - (fact(n) * residue)
    return ans

#for n in range(1,10):
#    print(fact(n))

string = ''
for each in perm(999999):
    string = string + str(each)
print(string)

