'''
2, 2
0, 8

2 + 6 = 8
'''

a, b = map(int, input().split())

a, b = a - 1, b - 1
print(abs((a // 4) - (b // 4)) + abs((a % 4) - (b % 4)))