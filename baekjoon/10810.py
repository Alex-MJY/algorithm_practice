'''
0 0 0 0 0
3 3 0 0 0
3 3 4 4 0
1 1 1 1 0
1 2 1 1 0
'''

n, m = map(int, input().split())
array = [0] * (n + 1)
for i in range(m):
    i, j, k = map(int, input().split())
    for z in range(i, j + 1):
        array[z] = k

for i in array[1:]:
    print(i, end=' ')