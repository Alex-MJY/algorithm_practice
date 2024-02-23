import sys
input = sys.stdin.readline

a_cnt, b_cnt = 0, 0
for i in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        continue
    elif a > b:
        a_cnt += 1
    else:
        b_cnt += 1
print(a_cnt, b_cnt)