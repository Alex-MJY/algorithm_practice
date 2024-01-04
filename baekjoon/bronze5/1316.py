num = int(input())
result = 0

for i in range(num):
    store = [None]
    word = str(input())
    for j in word:
        if j == store[-1]:
            continue
        store.append(j)
    if len(store) == len(set(store)):
        result += 1
print(result)