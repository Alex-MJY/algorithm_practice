"""
커리큘럼 :
컴공 강의를 듣고 있다. 선수강의가 있는 강의도 존재한다. 총 N개의 강의를 들으려고 하고, 여러 개의 강의를 동시에 들을 수 있다.
N개의 강의에 대하여 수강하기까지 걸리는 최소시간을 구하여라.
"""
from collections import deque
import copy

v = int(input())
indegree = [0] * (v + 1)
graph = [[] for _ in range(1 + v)]
time = [0] * (v + 1)

for i in range(1, v + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1 : -1]:
        indegree[i] += 1
        graph[x].append(i)
        
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in range(1, v + 1):
        print(result[i])
topology_sort()