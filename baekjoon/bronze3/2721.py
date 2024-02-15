# import sys
# input = sys.stdin.readline

# for i in range(int(input())):
#     n = int(input())
#     t = 0
#     sum = 0
#     for j in range(1, n + 1):
#         for k in range(1, j + 2):
#             t += k
#         sum += j * t
#         t = 0
#     print(sum)


for _ in range(int(input())):
    n = int(input())
    res = sum(k * sum(range(k + 2)) for k in range(1, n + 1))
    print(res)