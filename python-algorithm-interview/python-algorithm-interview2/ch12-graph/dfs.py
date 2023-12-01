'''일반적으로 스택으로 구현하며, 재귀를 이용하면 더 간단하게 구현할 수 있다.'''


graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

# recursive
def recursive_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered


# stack
# 스택을 이용해 모든 인접 간선을 추출하고 다시 도착점인 정점을 스택에 삽입하는 구조.   
# 재귀구조보다 직관적이고 실행 속도도 더 빠르다.
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

print(f"recursive dfs : {recursive_dfs(1)}")
print(f"iterative dfs : {iterative_dfs(1)}")


# 재귀 DFS는 사전식 순서로 방문한 데 반해 반복 DFS는 역순으로 방문했다
# 스택으로 구현하다 보니 가장 마지막에 삽입된 노드부터 꺼내서 반복하게 되고 이 경우 인접 노드에서 가장 최근에 담긴 노드,
# 즉 가장 마지막부터 방문하기 때문이다. 


'''
백트래킹은 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기(백트랙)해 정답을 찾아가는 알고리즘이다.
제약 충족 문제(Constraint Satisfaction Problems)에 특히 유용하다.
백트래킹은 dfs보다 더 광의의 의미를 지닌다. 즉 백트캐링은 dfs와 같은 방식으로 탐색하는 모든 방법을 뜻하며, dfs는 백트래킹의 골격을 이루는 알고리즘이다.
백트래킹은 가보고 되돌아오고를 반복한다. 최악의 경우 모든 경우를 다 거친 다음에 도착할 수 있다. (브루트 포스와 유사하다.)
'''