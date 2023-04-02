class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            fuel = 0
            for i in range(start, len(gas) + start):
                index = i % len(gas)

                can_travel = True
                if gas[index] + fuel < cost[index]:
                    can_travel = False
                    break
                else:
                    fuel += gas[index] - cost[index]
            if can_travel:
                return start
        return -1
    
# 주유소의 경로는 원형으로 연결되어 있으므로, 모듈로 연산을 하여 인덱스를 다시 0으로 지정할 수 있게 한다.
# 모든 주유소를 방문 가능한지 점검하고, 가능할 경우 이 문제에서는 출발점이 유일하다는 제약이 있기 때문에 가능한 지점을 찾으면 바로 리턴한다.
# 루프가 중첩되어 있으므로 O(n^2)이다.