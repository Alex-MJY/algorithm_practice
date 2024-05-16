while True:
    i1, i2, i3 = map(str, input().split())
    if i1 == "0" and i2 == "W" and i3 == "0":
        break
    if i2 == "W":
        result = int(i1) - int(i3)
        if result >= -200:
            print(result)
        else:
            print("Not allowed")
    if i2 == "D":
        result = int(i1) + int(i3)
        print(result)