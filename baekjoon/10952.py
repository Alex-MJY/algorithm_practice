array = []

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    array.append(a + b)
    
for i in array:
    print(i)