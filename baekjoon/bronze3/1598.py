'''
2, 2
0, 8

2 + 6 = 8
'''

a, b = map(int, input().split())

a1 = a // 4 # 2

if a % 4 != 0:
    a2 = (a % 4) - 1 # 2
else:
    a2 = 3
    
    
    
b1 = b // 4  # 8
if b % 4 != 0:
    b2 = (b % 4) - 1 # 0
    
else:
    b2 = 3
    
print(abs(a1 - b1) + abs(a2 - b2))