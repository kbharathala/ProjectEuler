list = []

for a in range(1,10,1):
    for b in range(1,22,1):
        if len(str(a**b)) == b:
            list.append(a**b)
print(len(list))
