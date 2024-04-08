import sys
input = sys.stdin.readline

s = int(input())
m = int(input())
l = int(input())
result = (s * 1) + (m * 2) + (l * 3)
if (result >= 10):
    print("happy")
else:
    print("sad")