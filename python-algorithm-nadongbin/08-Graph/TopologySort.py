'''
위상 알고리즘(정렬 알고리즘)
위상 정렬 : 방향 그래프의 모든 노드를 '방향성에 거르지 않도록 순서대로 나열하는 것'
진입 차수 : 특정 노드로 들어오는 간선의 개수

1. 진입차수가 0인 노드를 큐에 넣는다
2. 큐가 빌 때까지 다음 과정 반복
    - 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
    - 새롭게 진입차수가 0이 된 노드를 큐에 넣는다
    
시간복잡도는 O(V + E). 모든 노드를 확인하면서 해당 노드에서 출발하는 간선을 차례대로 제거하기 때문에 노드와 간선의 개수만큼 시간이 듬
'''
from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1)  # 진입차수 0으로 초기화
graph = [[] for i in range(v + 1)]  # 간선정보를 담기 위한 연결 리스트 초기화

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def topology_sort():
    result = []
    q = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=" ")
topology_sort()