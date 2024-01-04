s = input()
result = 0
array = s.split(' ')
for i in array:
    if i.isalnum():
        result += 1
print(result)