n = str(input())
counter = 0
for i in n:
    print(i, end='')
    counter += 1
    if counter >= 10:
        counter = 0
        print()
