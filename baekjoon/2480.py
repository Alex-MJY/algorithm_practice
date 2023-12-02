array = list(map(int, input().split()))

if len(set(array)) == 1:
    print((max(array) * 1000) + 10000)

if len(set(array)) == 2:
    array.sort()
    print((array[1] * 100) + 1000)    
    
if len(set(array)) == 3:
    print(max(array) * 100)