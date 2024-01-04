import sys
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
find = int(sys.stdin.readline())
result = 0

for i in range(len(array)):
    if array[i] == find:
        result += 1
        
print(result)