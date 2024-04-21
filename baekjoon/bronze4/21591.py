import sys
input = sys.stdin.readline

w1, h1, w2, h2 = map(int, input().split())

if (w1 - 1 > w2) and (h1 - 1 > h2):
    print(1)
else:
    print(0)