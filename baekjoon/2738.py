n, m = map(int, input().split())

array_a = []
array_b = []

for i in range(n):
    array_a.append(list(map(int, input().split())))
for i in range(n):
    array_b.append(list(map(int, input().split())))
for i in range(n):
    c = []
    for j in range(m):
        c.append(array_a[i][j] + array_b[i][j])
    print(*c)