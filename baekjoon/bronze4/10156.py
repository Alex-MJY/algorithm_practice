price, snack, money = map(int, input().split())
result = (price * snack) - money
if result < 0:
    print(0)
else:
    print(result)