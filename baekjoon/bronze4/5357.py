n = int(input())
for i in range(n):
    s = str(input())
    array = [None]
    for j in s:
        if array[-1] == j:
            continue
        array.append(j)
    print(''.join(array[1:]))