# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))

# if a[0] == b[0]:
#     if c[1] == a[1] and c[1] != b[1]:
#         print(c[0], b[1])
#     elif c[1] != a[1] and c[1] == b[1]:
#         print(c[0], a[1])
        
# elif a[0] == c[0]:
#     if b[1] == a[1] and b[1] != c[1]:
#         print(b[0], c[1])
#     elif b[1] != a[1] and b[1] == c[1]:
#         print(b[0], a[1])
        
# elif b[0] == c[0]:
#     if a[1] == b[1] and a[1] != c[1]:
#         print(a[0], c[1])
#     elif a[1] != b[1] and a[1] == c[1]:
#         print(a[0], b[1])

'''
위에도 맞으나 보기 더럽다.
'''

x_arr = []
y_arr = []

for i in range(3):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)
    
for i in range(3):
    if x_arr.count(x[i]) == 1:
        x = x_arr[i]
    if y_arr.count(y[i]) == 1:
        y = y_arr[i]
print(x, y)