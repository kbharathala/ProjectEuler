coin_list = [200,100,50,20,10,5,2]

def coin_ways(total):
    ans = 0
    hold = total
    for coin in coin_list:
        for values in range(0,int(hold/coin)+1):
            hold = hold - int(hold/coin) * coin
            if coin == 2:
                ans = ans + hold
            
