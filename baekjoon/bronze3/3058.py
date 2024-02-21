import sys
input = sys.stdin.readline

for i in range(int(input())):
    arr = list(map(int, input().split()))
    min_n = 100
    total_n = 0
    for i in arr:
        if i % 2 == 0:
            total_n += i
            if i < min_n:
                min_n = i
    print(total_n, min_n)