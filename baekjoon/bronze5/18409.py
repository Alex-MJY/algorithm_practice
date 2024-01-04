n = int(input())
s = str(input())
result = 0
for i in s:
    if i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o':
        result += 1
print(result)