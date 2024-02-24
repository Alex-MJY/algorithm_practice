import sys
input = sys.stdin.readline

for i in range(int(input())):
    arr = list(map(int, input().split()))
    print(sum(arr))