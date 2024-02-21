n, w, h = map(int, input().split())
for i in range(n):
    num = int(input())
    if num ** 2 <= (w ** 2) + (h ** 2):
        print("DA")
    else:
        print("NE")