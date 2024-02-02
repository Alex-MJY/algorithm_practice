counter = 0
for i in range(int(input())):
    s = str(input())
    day = int(s[2:])
    if day <= 90:
        counter += 1
print(counter)