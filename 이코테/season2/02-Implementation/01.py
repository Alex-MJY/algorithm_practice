# 상하좌우

'''
input:
- 첫째 줄에 공간의 크기를 나타내는 n이 주어진다
- 둘째 줄에 여행가가 이동할 계획서 내용이 주어진다

output:
- 여행가가 최종적으로 도착할 지점의 좌표(x, y)를 공백으로 구분하여 출력
'''

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)