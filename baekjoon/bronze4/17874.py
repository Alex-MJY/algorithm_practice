import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

if b <= a - b:
    b = a - b

if c <= a - c:
    c = a - c
    
print(4 * b * c)