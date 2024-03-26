a, b = map(str, input().split())
aa = int("0b" + a, 2)
bb = int("0b" + b, 2)
print(bin(aa + bb)[2:])

