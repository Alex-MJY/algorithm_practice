a, b = map(int, input().split())
num = 0

if b - 45 >= 0:
    b -= 45
    print(a, b)
else:
    num = b - 45
    a -= 1
    b = 60 - abs(num)
    if a == -1:
        a = 23
    print(a, b)