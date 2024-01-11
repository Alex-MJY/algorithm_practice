n = int(input())
array = []
while n != 0:
    if n >= 5:
        n -= 5
        array.append("V")
    elif n < 5:
        n -= 1
        array.append("I")
    else:
        break
for i in array:
    print(i, end='') 