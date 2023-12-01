'''
크루스칼 알고리즘(그리디 알고리즘)
1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
    - 사이클을 발생하는 경우 신장트리에 포함시키지 않고 발생시키지 않는 경우 신장트리에 포함
3. 모든 간선에 대하여 2번 과정 반복

간선의 개수가 E개일 때, O(ElogE)의 시간복잡도를 가진다.
시간이 가장 오래걸리는 부분은 간선을 정렬하는 작업. 크루스칼 내부에서 사용되는 서로소 집합 알고리즘의 시간 복잡도는 무시 가능하다.
'''
# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())  

# 부모 테이블 초기화
parent = [0] * (v + 1)  

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i
    
# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    
# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며 사이클이 발생하지 않는 경우에만 집합에 포함
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)