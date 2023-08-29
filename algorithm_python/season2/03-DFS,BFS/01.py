# 음료수 얼려 먹기
'''
input : 
- 첫 번째 줄ㅔ 얼ㅡㅁ 틀의 세로 길이 n과 가로 길이 m이 주어진다.
- 두 번째 줄부터 n + 1번째까지 얼음 틀의 형태가 주어진다.
- 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
output : 
- 한 번에 만들 수 있는 아이스크림 개수를 출력한다.
'''

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 재귀 호출
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            
print(result)