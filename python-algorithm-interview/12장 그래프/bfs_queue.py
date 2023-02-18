graph = {
    1 : [2,3,4],
    2 : [5],
    3 : [5],
    4 : [],
    5 : [6,7],
    6 : [],
    7 : [3],
}

# 모든 인접 간선을 추추출하고 도착점인 정점을 큐에 삽입한다.
def iterative_bfs(start_v):
    discoverd = [start_v]
    queue = [start_v]
    
    while queue:
        v = queue.pop()
        for w in graph[v]:
            if w not in discoverd:
                discoverd.append(w)
                queue.append(w)
    return discoverd

print(f"iterative bfs : {iterative_bfs(1)}")