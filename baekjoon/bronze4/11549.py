tea = int(input())
answer = list(map(int, input().split()))
counter = 0
for i in answer:
    if i == tea:
        counter += 1
print(counter)