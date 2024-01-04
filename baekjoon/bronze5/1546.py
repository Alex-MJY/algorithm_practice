import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
max_n = max(array)
result = 0

for i in range(n):
    div_n = array[i] / max_n * 100
    result += div_n
    
print(result / n)