'''
시간복잡도 : O(N^3)
다익스트라 알고리즘은 출발 노드가 1개라서 다른 노드까지의 최단 거리를 저장하기 위해 1차원 리스트를 사용.
플로이드 워셜 알고리즘은 모든 노드에 대하여 다른 모든 노드로 가는 최단거리를 담아야 하기 때문에 2차원 리스트에 '최단거리' 저장. 
'''

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
            
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("Infinity", end = " ")
        else:
            print(graph[a][b], end = " ")