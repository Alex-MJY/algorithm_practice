array = []
while True:
    try:
        n, s = map(int, input().split())
        array.append(s // (n + 1))
    except EOFError:
        [print(i) for i in array]
        break