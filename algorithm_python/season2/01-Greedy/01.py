# 거스름돈

n = int(input("how much? "))
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin
    
print(count)