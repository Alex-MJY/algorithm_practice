import sys
input = sys.stdin.readline

for i in range(int(input())):
    s = str(input())
    print(s[0].upper() + s[1:])