'''
개선된 다익스트라 알고리즘. 이전 버전은 선형적으로 모두 검색했기 때문에 O(v^2)의 시간 복잡도 보장. 
heapq를 사용하면 O(ElogV)를 보장. 여기서 V는 노드의 개수, E는 간선의 개수를 의미.
힙 자료구조는 특정 노드까지의 최단 거리에 대한 정보를 힙에 담아 처리하기 때문에 출발 노드로부터 가장 거리가 짧은
노드를 더 빨리 찾을 수 있다. 이 과정에서 선형 시간이 아닌 로그 시간이 걸린다. 
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("Infinity")
    else:
        print(distance[i])