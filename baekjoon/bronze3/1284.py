# import sys
# input = sys.stdin.readline

while True:
    s = int(input())
    if s == 0:
        break
    counter = 0
    for i in str(s):
        if i == '0':
            counter += 4
        elif i == '1':
            counter += 2
        else:
            counter += 3
    print(counter + (len(str(s)) - 1) + 2)