while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    n = 1
    for i in range(arr[0]):
        n = n * arr[(i * 2) + 1] - arr[(i * 2) + 2]
    print(n)