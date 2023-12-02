total_price = int(input())
items = int(input())

p = 0

for i in range(items):
    a, b = map(int, input().split()) # a is price, b is number of items
    p += (a * b)
    
if p == total_price:
    print("Yes")
else:
    print("No")