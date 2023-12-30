while True:
    n = int(input())
    if n == 0:
        break
    result = 0
    for i in range(n, 0, -1):
        result += i
    print(result)