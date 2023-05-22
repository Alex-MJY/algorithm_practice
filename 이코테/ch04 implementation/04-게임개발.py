'''
캐릭터가 있는 맵은 정사각형으로 이뤄진 N*M 크기의 직사각형. 각각의 칸은 육지 또는 바다. 캐릭터는 동서남북 중 한 곳을 바라본다.
맵의 각 칸은 (A,B)로 나타내고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수.
상하좌우로 움직일 수 있고, 바다로는 갈 수 없다. (맵 외부도 이동 불가능)

1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계)부터 차례대로 갈 곳을 정한다.
2. 캐릭터의 왼쪽 방향에 가보지 않은 칸이 존재하면, 왼쪽 방향으로 회전하고 한 칸 전진. 왼쪽 방향에 가보지 않은 칸이 없다면, 회전만 수행하고 1단계로 돌아간다.
3. 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 경우, 바라보는 방향을 유지하고 한 칸 뒤로 가고 1단계로 돌아간다. 뒤쪽 방향이 바다인 경우 움직임을 멈춘다.

캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만들어라.
'''

# 0:북, 1:동, 2:남, 3:서
# 0: 육지, 1: 바다

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

# 현재 방문한 위치를 저장하기 위한 맵을 생성
d = [[0] for _ in range(n)]
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
# define north, east, south, west
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# turn left
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
# simulation
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
        
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
        
print(count)