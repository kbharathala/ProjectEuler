def pentagonal(n):
    return (n*(3*n-1)/2)

def hexagonal(n):
    return (n*(2*n-1))

list_pent = []
list_hex = []

for i in range(1,40000,1):
    list_pent.append(pentagonal(i))
    list_hex.append(hexagonal(i))

a = 0
for hexa in list_hex:
    a = a + 1
    if a % 1000 == 0:
        print(a)
    if hexa in list_pent:
        print(hexa)
