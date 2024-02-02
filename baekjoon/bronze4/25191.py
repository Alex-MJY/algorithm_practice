n = int(input()) # chicken
a, b = map(int, input().split()) # coke, beer
eat = a // 2 + b
if eat <= n:
    print(eat)
else:
    print(n)