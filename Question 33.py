def num_picker(n):
    list = []
    for denominator in range(11,n+1):
        for numerator in range(10,denominator):
            list.append([numerator,denominator])
    return list

def equal(list):
    num = list[0]
    denom = list[1]
    if denom % 10 == 0:
        return False
    real = num/denom
    if (int(str(num)[1])) != int((str(denom)[0])):
        return False
    fake = (int(str(num)[0]))/int((str(denom)[1]))
    if real == fake:
        fake = (int(str(num)[1]))/int((str(denom)[1]))
        if real != fake:
            fake = (int(str(num)[0]))/int((str(denom)[0]))
            if real != fake:
                return(num,denom)
            else:
                return False
            
        else:
            return False
    else:
        return False

for each in num_picker(100):
    if equal(each) != False:
        print(equal(each))
    
        
    
