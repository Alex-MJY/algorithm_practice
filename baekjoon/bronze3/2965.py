'''
사막에 캥거루 세 마리. 사막에 수직선 하나, 캥거루는 서로 다른 한 좌표위에 있다.
한 번 움직일 때, 바깥쪽 두 캥거루 중 한마리가 다른 두 캥거루 사이의
정수 좌표로 점프. 한 좌표 위에 두 마리 존재 불가능.


3 5 9
6 5 9
6 7 9
8 7 9
123


2 5 8
6 5 8
6 7 8
'''
# a, b, c = map(int, input().split())

# if abs(a - b) == abs(b - c):
#     if abs(a - b) == 1:
#         print(0)
#     else:
#         print(abs(a - b) - 1)
# elif abs(a - b) < abs(b - c):
#     print(abs(b - c) - 1)
# else:
#     print(abs(a - b) - 1)
    
    
a, b, c = map(int, input().split())
print(max(abs(a - b),abs(b - c)) - 1)