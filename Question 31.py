count = 0
for a in range(2):
    if (200*a) > 200:
        break
    for b in range(3):
        if (200*a + 100*b) > 200:
            break                
        for c in range(5):
            if (200*a + 100*b + 50*c) > 200:
                break                        
            for d in range(11):
                if (200*a + 100*b + 50*c + 20*d) > 200:
                    break
                for e in range(21):
                    if (200*a + 100*b + 50*c + 20*d + 10*e) > 200:
                        break
                    for f in range(41):
                        if (200*a + 100*b + 50*c + 20*d + 10*e + 5*f) > 200:
                            break
                        for g in range(101):
                            if (200*a + 100*b + 50*c + 20*d + 10*e + 5*f
                                  + 2*g) > 200:
                                break                            
                            for h in range(201):
                               if (200*a + 100*b + 50*c + 20*d +
                                    10*e + 5*f + 2*g + 1*h) > 200:
                                    count += 1
                                    break      
                               
                                   
print(count)
