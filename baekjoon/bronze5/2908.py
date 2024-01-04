a, b = map(str, input().split())
a, b = list(a), list(b)
a.reverse()
b.reverse()
a = int(''.join(a))
b = int(''.join(b))

print(max(a, b))