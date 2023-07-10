graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

# 스택을 이용하는 dfs와는 달리, bfs를 반복 구조로 구현할 때는 큐를 이용한다.
# 리스트 자료형을 사용했지만 pop(0)과 같은 큐의 연산만을 사용했다. (deque 사용 가능)
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered


# bfs는 재귀로 동작하지 않는다. 큐를 이용하는 반복 구현만 가능하다.