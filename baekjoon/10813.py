n, m = map(int, input().split())

array = [0] * n
for i in range(n):
    array[i] = i + 1
    
for i in range(m):
    x, y = map(int, input().split())
    array[x - 1], array[y - 1] = array[y - 1], array[x - 1]

for i in array:
    print(i, end = " ")