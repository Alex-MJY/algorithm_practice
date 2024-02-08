import sys
input = sys.stdin.readline

num = int(input())
sum = 1
for _ in range(num):
    tempNum = int(input())
    sum += tempNum
print(sum - num)