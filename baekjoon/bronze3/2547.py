import sys
input = sys.stdin.readline

for _ in range(int(input())):
    _ = input()
    n = int(input())
    candy = 0
    for _ in range(n):
        candy += int(input())
    if candy % n == 0:
        print("YES")
    else:
        print("NO")