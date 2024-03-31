import sys
input = sys.stdin.readline
x = list(map(int, input().split()))
y = list(map(int, input().split()))
counter = 0

for i in range(len(x)):
    if x[i] < y[i]:
        counter += y[i] - x[i]
        
print(counter)