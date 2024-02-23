import sys
input = sys.stdin.readline
counter = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break
    n1 = n0 * 3
    if n1 % 2 == 0:
        n2 = n1 // 2
        print(f"{counter}. even", end=' ')
    else:
        n2 = (n1 + 1) // 2
        print(f"{counter}. odd", end=' ')
    n3 = n2 * 3
    counter += 1
    print(n3 // 9)
    