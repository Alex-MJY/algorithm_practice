arr = []
for i in range(int(input())):
    a, b = map(int, input().split()) # a=가게까지가는데걸리는시간, b=현재시점에서빵이들어올때까지시간
    if a <= b:
        arr.append(b)

if len(arr) == 0:
    print(-1)
else:
    print(min(arr))