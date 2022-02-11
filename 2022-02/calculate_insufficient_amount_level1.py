def solution(price, money, count):
    
    sum_price = 0
    
    for i in range(1,count+1):
        
        sum_price += price * i
        
    if sum_price >= money :
        return sum_price - money
    else :
        return 0


price = 3

money = 20

count = 4

print(solution(price,money,count))