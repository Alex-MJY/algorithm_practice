'''k번 이상 등장하는 요소를 추출하라.'''

# Counter를 이용한 음수 순 추출
# 요소의 값을 키로 하는 해시 테이블을 만들고 여기에 빈도 수를 저장한 다음
# 우선순위 큐(heapq)를 이용해 k번만큼 추출하면 k번 이상 등장하는 요소를 쉽게 추출할 수 있다.
# 힙에 삽입하는 방식은 두가지가 있는데, 첫째는 일반적인 파이썬의 리스트에 모두 삽입한 다음
# 마지막에 heapify()를 하는 방식과, 매번 heappush()를 하는 방식이다.
# heappush()로 삽입하면 매번 heapify()가 일어나기 때문에 별도로 처리할 필요가 없다.
# heapq.heappush(freqs_heap, (-freqs[f], f))는 빈도수를 키로 하고, freqs의 키를 값으로 했다.
# 즉, 키/값을 바꿔서 힙에 추가했다. 힙은 키 순서대로 정렬되기 때문에 이를 위해 빈도 수를 키로 했다.
# 값을 음수로 저장했는데, heapq 모듈은 최소 힙만 지원하기 때문이다. 
# 마지막으로 heappop()으로 k번만큼 값을 추출하면 결과를 얻을 수 있다.
import collections
import heapq

class Solution1:
    def topKFrequent(self, nums: list, k: int) -> list:
        freqs = collections.Counter(nums)
        freqs_heap = []

        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = list()
        # k번 만큼 추출, 최소 힙(MinHeap)이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk
    
    
# pythonic
# collections.Counter는 most_common()이라는 빈도수가 높은 순서대로 아이템을 추출하는 기능을 제공한다.

# zip()은 2개 이상의 시퀀스를 짧은 길이를 기준으로 일대일 대응하는 새로운 튜플 시퀀스를 만든다.
# zip()은 제너레이터를 리턴한다. 실제값을 추출하기 위해서는 list()로 한 번 더 묶어준다.

# 파이썬에서 애스터리스크(*)는 pointer가 아닌 시퀀스를 풀어헤치는 unpacking을 수행한다. 
# 언패킹뿐만 아니라 함수의 파라미터가 되었을 때는 반대로 패킹도 가능하다. 
class Solution2:
    def topKFrequent(self, nums: list, k: int) -> list:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]