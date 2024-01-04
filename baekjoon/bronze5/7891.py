num = int(input())
array = []
for i in range(num):
    a, b = map(int, input().split())
    result = a + b
    array.append(result)
# print(*array)
for i in array:
    print(i)