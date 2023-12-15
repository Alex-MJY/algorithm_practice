n = int(input())
array = []
for i in range(n):
    a, b = map(str, input().split())
    s = str()
    for j in b:
        j = j * int(a)
        s += j
    array.append(s)

for i in array:
    print(i)