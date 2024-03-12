board = [[], [], [], [], [], [], [], []]

counter = 0

for i in range(8):
    s = str(input())
    if i % 2 == 0: 
        ss = s[::2]
    else:
        ss = s[1::2]
    for j in ss:
        if j == 'F':
            counter += 1
print(counter)