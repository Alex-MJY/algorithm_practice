# 미로 탈출
'''
input :
- 첫째 줄에 두 정수 n, m이 주어진다. n개의 줄에는 m개의 정수로 미로의 정보가 주어진다. 각각의 수들은 공백 없이 붙여서 입력된다. (1은 갈 수 있고, 0은 막힌 곳)
output :
- 첫째 줄에 최소 이동 칸의 개수를 출력한다.
'''

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
# u, d, l, r
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]

print(bfs(0, 0))