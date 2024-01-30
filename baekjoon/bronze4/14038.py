win = 0
for i in range(6):
    s = str(input())
    if s == 'W':
        win += 1
    

if 6 >= win >= 5:
    print(1)
if 4 >= win >= 3:
    print(2)
if 2 >= win >= 1:
    print(3)
if win == 0:
    print(-1)