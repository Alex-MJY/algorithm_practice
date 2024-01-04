n = int(input())
array = []
for i in range(n):
    password = input()
    if 6 <= len(password) <= 9:
        array.append("yes")
    else:
        array.append("no")
for i in array:
    print(i)