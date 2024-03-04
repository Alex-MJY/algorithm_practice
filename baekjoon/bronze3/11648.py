# import sys
# input = sys.stdin.readline

n = str(input())
counter = 0
num = 1
while (int(n) >= 10):
    for i in str(n):
       num *= int(i)
    n = str(num)
    num = 1
    counter += 1
print(counter)