# 뱀 (p327, p521)

'''
도스게임이 있다. 뱀이 기어 다니는데, 사과를 먹으면 뱀의 길이가 늘어난다. 뱀이 기어다니다가 벽 또는 자신의 몸과 부딪히면 게임이 끝난다.
게임은 NxN 정사각 보드 위에서 진행. 몇몇 칸에는 사과가 놓여져 있다. 게임을 시작할 때 뱀은 맨 위 맨 좌측에 위치. 뱀의 길이는 1. 뱀은 처음에 오른쪽을 향한다.
매 초마다 이동하는데 아래의 규칙을 따른다.
    - 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킨다.
    - 이동한 칸에 사과가 있다면, 그 칸의 사과는 없어지고 꼬리는 움직이지 않는다.
    - 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비운다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동 경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산해라.

입력조건 : 첫줄에 보드의 크기 n, 두번째 줄에 사과의 개수 k, 다음 k개 줄에 사과 위치(행, 열), 다음 줄에 방향 변환 횟수 l, l개의 변환 정보 (x:int, c:char)
'''

n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]  # map info
info = []  # direction info
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()   # c가 L이면 왼쪽, D면 오른쪽 회전
    info.append((int(x), c))
    
# 처음에는 오른쪽을 보고 있으므로 (동, 남, 서 북) / 보는 기준으로 동쪽 이동은 아래로 이동
dx = [0, 1, 0, -1]  
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
        
def simulate():
    x, y = 1, 1  # 뱀 시작 지점
    data[x][y] = 2  # 뱀 현재 위치 2로 표시
    direction = 0  # 처음에는 동쪽을 보고있음
    time = 0  # 시작한 뒤에 지난 시간
    index = 0  # 다음에 회전할 정보
    q = [(x, y)]  # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
    while True:
        nx = x + dx[direction]
        ny = x + dy[direction]
        # 맴 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else: # 벽이나 뱀의 몸통과 부딪혔다면
            time += 1
            break
        x, y = nx, ny  # 다음 위치로 머리 이동
        time += 1
        if index < 1 and time == info[index][0]:  # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][0])
            index += 1
    return time
print(simulate())