import sys
input = sys.stdin.readline

for i in range(int(input())):
    money = [None, None, None, None]
    n = int(input())

    if n % 25 >= 0:
        money[0] = n // 25
        n -= (25 * (n // 25))
    if n % 10 >= 0:
        money[1] = n // 10
        n -= (10 * (n // 10))
    if n % 5 >= 0:
        money[2] = n // 5
        n -= (5 * (n // 5))
    if n % 1 >= 0:
        money[3] = n // 1
    
    print(*money)