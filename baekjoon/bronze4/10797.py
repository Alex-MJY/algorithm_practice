date = int(input())
cars = list(map(int, input().split()))
counter = 0
for i in cars:
    if str(i)[-1] == str(date)[-1]:
        counter += 1
print(counter)