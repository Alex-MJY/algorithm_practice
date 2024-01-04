import sys

n = int(sys.stdin.readline())
array = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    array.append(a + b)
    
for i, e in enumerate(array):
    print(f"Case #{i + 1}: {e}")