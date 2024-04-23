import sys

n = int(sys.stdin.readline())

counter = 1
emp = 0
for i in range(n, 0, -1):
    result = (2 * n) - counter
    counter += 2
    print(emp * ' ' + result * '*')
    emp += 1