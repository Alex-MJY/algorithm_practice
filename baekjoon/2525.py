h, m = map(int, input().split())
c = int(input())

x = m + c
if x < 60:
    print(h, x)
else:
    num = x // 60
    m = x % 60
    if h == 23:
        h = -1
    if m + c == 60:
        print(h + num + 2, m)
    print(h + num, m)