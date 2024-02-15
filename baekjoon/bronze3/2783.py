import sys
input = sys.stdin.readline

x, y = map(int, input().split())
arr = [x / y]
for _ in range(int(input())):
    a,b = map(int, input().split())
    arr.append(a / b)

print("%.2f" % (min(arr)*1000))