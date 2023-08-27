# graph는 node(vertex)와 edge로 구성된다. 두 노드가 간선으로 연결되어 있으면 인접(adjacent)되어 있다고 표현한다.
# 인접 행렬(adjacency matrix) 또는 인접 리스트(adjacency list)로 구현할 수 있다.


# 인접 행렬 방식 예제
INF = 999999999 # 무한의 비용

graph1 = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph1)

# 인접 리스트 방식 예제
graph2 = [[] for _ in range(3)] # 행(row)이 3개인 2차원 리스트로 인접 리스트 표현

# 노드 0에 연결된 노드 정보 저장 (노드, 거리)
graph2[0].append((1, 7))
graph2[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장
graph2[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장
graph2[2].append((0, 5))

print(graph2)



# 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비된다. 인접 리스트 방식은 연결된 정보만을 저장하기 때문에 상대적으로 효율적이다.
# 하지만 연결된 데이터를 하나씩 확인해야 하기 때문에 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다. 

'''
DFS는 스택 자료구조를 이용하며 동작 과정은 다음과 같다.
1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
3. 2번의 과정을 수행할 수 없을 때까지 반복한다.
'''

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
graph3 = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph3, 1, visited)