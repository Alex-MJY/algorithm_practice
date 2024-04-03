arr = []
for i in range(6):
    arr.append(int(input()))
    
a = (arr[0] * 3) + (arr[1] * 2) + (arr[2] * 1)
b = (arr[3] * 3) + (arr[4] * 2) + (arr[5] * 1)

if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('T')