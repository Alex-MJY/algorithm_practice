import collections

class Solution:
    def leastInterval(self, tasks: list, n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            # 개수 순 추출
            for task, _ in counter.most_common(n+1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            if not counter:
                break

            result += n - sub_count + 1
        return result
    

# 먼저, 우선순위 큐를 사용해 가장 개수가 많은 아이템부터 하나씩 추출해야 하는데, 문제는 전체를 추출해야 하는 게 아니라 
# 하나만 추출하고 빠진 개수를 업데이트할 수 있는 구조가 필요하다는 점이다.
# collections.Counter의 most_common은 최대힙과 같은 역할을 한다. 그러나 pop() 으로 추출되는 것은 아니기 때문에
# subtrack(task)를 지정해 1개씩 개수를 별도로 줄여나간다.

# 빈 컬렉션을 더할경우 0 이하인 아이템을 목록에서 아예 제거해버린다. 매우 유용한 Hack이다.


# 아무리봐도 모르겠음;;    