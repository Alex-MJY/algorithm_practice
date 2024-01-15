import sys
n = int(sys.stdin.readline())
for i in range(1, n + 1):
    print(i, end=" ")
    if i % 6 == 0 and i != n:
        print("Go!", end=" ")
print("Go!")