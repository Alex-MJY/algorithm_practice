# d, h, m = map(int, input().split())

# time = (d - 11) * 60 * 24 + (h - 11) * 60 + (m - 11)

# if time >= 0:
#     print(time)
# else:
#     print(-1)

d, h, m = map(int, input().split())
time1 = d * 24 * 60 + h * 60 + m
time2 = 11 * 24 * 60 + 11 * 60 + 11
result = time1 - time2
if result >= 0:
    print(result)
else:
    print(-1)