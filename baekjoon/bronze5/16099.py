n = int(input())
array = []
for i in range(n):
    lt, wt, le, we = map(int, input().split())
    if lt * wt > le * we:
        array.append("TelecomParisTech")
    elif lt * wt < le * we:
        array.append("Eurecom")
    elif lt * wt == le * we:
        array.append("Tie")
for i in array:
    print(i)