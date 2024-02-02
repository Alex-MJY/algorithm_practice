coupon = int(input())
price = int(input())
result = []

if coupon >= 20:
    counter1 = price - (price * 0.25)
    counter2 = price - 2000
    result.append(min(counter1, counter2))
if 20 > coupon:
    counter1 = price - 2000
    counter2 = price - (price * 0.1)
    result.append(min(counter1, counter2))
if 15 > coupon:
    counter1 = price - 500
    counter2 = price - (price * 0.1)
    result.append(min(counter1, counter2))
if 10 > coupon:
    result.append(price - 500)
if 5 > coupon:
    result.append(price)
    
print(int(min(result)))