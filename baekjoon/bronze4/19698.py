'''
7 17 11 5
17 // 5 = 3
11 // 5 = 2
3 * 2 = 6

'''


n, w, h, l = map(int, input().split())
result = (w // l) * (h // l)
if n < result:
    print(n)
else:
    print(result)