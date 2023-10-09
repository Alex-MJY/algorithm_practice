# 전보
'''
어떤 나라에 N개의 도시가 있다. x도시에서 y도시에 전보를 보낼 경우 통로가 설치되어야 한다. 
어느 날 c도시에 위급 상황 발생. c에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 전보를 많이 퍼져나가게 하려고 한다.
각 도시의 번호와 통로가 설치되어 있는 정보가 주어져졌을 때, 메시지를 받게 되는 도시의 개수는 총 몇 개이며, 모두 메시지를 받는데 걸리는 시간은?
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
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

count = 0
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(d, max_distance)
print(count - 1, max_distance)