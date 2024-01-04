'''
1 2 3 4 5
2 1 3 4 5
2 1 4 3 5
3 4 1 2 5
3 4 1 2 5
'''
import sys

n, m = map(int, sys.stdin.readline().split())

array = [i for i in range(1, n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a == b:
        continue
    rev = array[a-1: b]
    rev.reverse()
    array[a-1 : b] = rev
    
for i in array:
    print(i, end=' ')