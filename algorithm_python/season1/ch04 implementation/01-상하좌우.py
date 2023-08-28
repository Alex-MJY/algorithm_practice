'''
n*n 크기의 정사각형 공간이 있다. 시작좌표는 항상 (1, 1)이다.
L, R, U, D 문자를 통해 4곳으로 이동할 수 있다. 정사각형 공간을 벗어나는 움직임은 무시된다. 
이동 계획서가 주어졌을 때 최종 도착 지점의 좌표를 출력해라.
'''

n = int(input())
plans = list(map(str, input().split()))

x, y = 1, 1

move_types = ['L', 'R', 'U', 'D']

# L, R, U, D
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


for plan in plans:
    if plan == 'L':
        if x > 1:
            x -= 1
    if plan == 'R':
        if x < n:
            x += 1
    if plan == 'U':
        if y < n:
            y += 1
    if plan == 'D':
        if y > 1:
            y -= 1
            
print(x, y)