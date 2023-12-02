# h, m = map(int, input().split())
# c = int(input())

# x = m + c
# if x < 60:
#     print(h, x)
# else:
#     num = x // 60
#     m = x % 60
#     if h == 23:
#         h = -1
#     h = h + num
#     if m + c == 60:
#         print(h + 2, m)
#     print(h, m)

h, m = map(int, input().split())
timer = int(input())

h += timer // 60  # timer가 60인 경우에만 1
m += timer % 60 

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24
    
print(h, m)