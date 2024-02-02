# import math

# n = int(input())
# fac_n = math.factorial(n)

# # week = 0
# i = 1
# while True:
#     week = i * 7 * 24 * 60 * 60
#     if week == fac_n:
#         break
#     i += 1
# print(i)

import sys
input = sys.stdin.readline

# 입력
n = int(input())

# 출력
res = 1
for i in range(11, n + 1):
    res *= i
print(6 * res)