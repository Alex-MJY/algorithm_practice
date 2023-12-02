x = int(input())
y = int(input())

if x >= 1:
    if y >= 1:
        print(1)
    elif y < 1:
        print(4)
elif x < 1:
    if y >= 1:
        print(2)
    elif y < 1:
        print(3)