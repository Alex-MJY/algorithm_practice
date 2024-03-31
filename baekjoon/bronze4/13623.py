import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())

if a == b == c:
    print("*")
elif a != b and b == c:
    print('A')
elif a != c and a == b:
    print('C')
elif b != c and a == c:
    print('B')