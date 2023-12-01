'''
전체 기름의 양이 전체 비용보다 클 경우 반드시 전체를 방문할 수 있는 출발점이 존재한다.
또한 출발점은 반드시 한 군데만 존재하게 된다.

if sum(gas) < sum(cost):
    return False
    
위처럼 비용이 더 클 때 리턴해버리면, 이제 반드시 존재하는 경우만 남아 있게 된다.
따라서 전체를 방문하면서 성립되지 않는 경우는 출발점을 한 칸씩 뒤로 밀어낸다.
한 번 이상은 반드시 성립되지 않는 지점이 존재한다.
이는 수학에서 귀류법으로 증명하는 것과 유사하다. 모순을 이끌어내 거짓인 경우를 제외하면,
가능한 지점은 제외하지 못한 지점이고, 자연스럽게 남은 곳이 정답이 된다.
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 모든 주유소 방문 가능 여부 판별
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0 
        for i in range(len(gas)):
            # 출발점이 안 되는 지점 판별
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start