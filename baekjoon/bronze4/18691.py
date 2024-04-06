import sys
input = sys.stdin.readline

for _ in range(int(input())):
    g, c, e = map(int, input().split())
    if e > c:
        if g == 1:
            print(e - c)
        elif g == 2:
            print((e - c) * 3)
        elif g == 3:
            print((e - c) * 5)
    else:
        print(0)