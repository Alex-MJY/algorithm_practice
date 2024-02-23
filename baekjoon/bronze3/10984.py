import sys
input = sys.stdin.readline

for i in range(int(input())):
    total = 0
    avg = 0
    for j in range(int(input())):
        a, b = map(float, input().split())
        total += a
        avg += a * b
    print(f"{total} {total / avg}") 