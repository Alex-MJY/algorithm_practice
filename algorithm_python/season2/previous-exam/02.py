# 곱하기 혹은 더하기 (312P, 507p)

s = str(input())
array = []
result = 0

for i in s:
    i = int(i)
    if i == 0 or result == 0:
        result += i
    else:
        result *= i
print(result)