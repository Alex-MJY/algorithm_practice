# 미래 도시
'''
도시에 1번부터 N번 까지의 회사가 있다. 회사끼리는 도로를 통해 연결. 판매원 A는 1번 회사에 위치. X번 회사에 방문해 물건 판매 계획.
연결된 2개의 회사는 양방향 이동 가능. 특정 회사와 다른 회사가 연결되어 있다면 이동 시간은 1로 취급. 
A는 소개팅도 할 예정. 상대는 K회사에 있음. 즉, A는 K번 회사에 방문 이후 X번 회사에 가는 게 목표. A가 회사 사이를 이동하는 최소 시간을 계산해라.
'''

INF = int(1e9)  # infinite
n, m = map(int, input().split())  # n is number of node, m is number of edge
graph = [[INF] * (n + 1) for _ in range(n + 1)]  # make two dimension list array, initialzied infinite

# cost from self to self is initialized 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0
            
# receives information about each edge and initializes it with that value
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
# input the node x to be passed through and the final destination node k
x, k = map(int, input().split())


# run Floyd Warshall algorithm accroding to the ignition equation
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
distance = graph[1][k] + graph[k][x]

if distance > INF:
    print("-1")
else:
    print(distance)