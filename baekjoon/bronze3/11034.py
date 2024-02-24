import sys
input = sys.stdin.readline


while True:
    try:
        a, b, c = map(int, input().split())
        print(max(b - a, c - b) - 1)
    except:
        break