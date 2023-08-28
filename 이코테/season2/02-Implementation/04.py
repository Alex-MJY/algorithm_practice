# 게임 개발
'''
input : 
- 첫째 줄에 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력.
- 둘째 줄에 게임 캐릭터가 있는 좌표 (A, B)와 바라보는 방향 d가 서로 공백으로 구분하여 주어진다. 방향 d는 4개가 주어진다.(북:0 동:1 남:2 서:3)
- 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. 맵의 외각은 항상 바다. (바다: 1, 육지: 0)
- 시작 칸은 항상 육지

output : 
- 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력
'''

n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]

# 좌표와 방향
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 방문 좌표

array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
# 시뮬레이션 시작
count = 0
turn_time = 9

while True:
    turn_left()
    nx = x + dx[direction] 
    ny = y + dy[direction]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    
    # 네 방향 모드 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = x - dy[direction]
        # 뒤로 갈 수 있으면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
        
print(count)