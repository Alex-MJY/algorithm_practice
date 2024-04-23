import sys
input = sys.stdin.readline

k, l = map(int, input().split())

cnt = 0
for i in range(2, l):
    if k % i == 0:
        cnt = 1
        print("BAD", i)
        break
if cnt == 0:
    print("GOOD")