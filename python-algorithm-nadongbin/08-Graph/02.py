"""
도시 분할 계획 :
마을은 n개의 집과 집을 연결하는 m개의 길로 이루어져 있다. 길은 어느방향이든 다닐 수 있고 길을 유지하는 유지비용이 든다.
마을을 2개로 분리하려고 한다. 분리된 마을 안의 집들이 서로 연결되어 있어야 한다. 마을엔 집이 하나 이상 있어야 한다.
분리된 마을 사이에 있는 길들은 필요없다.

a, b, c : a집부터 b집을 연결하는 길의 유지비 c
"""
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

edges = []
result = 0

for _ in range(e):  # 간선 정보 입력받기
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    
edges.sort()
last = 0  # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
print(result - last)