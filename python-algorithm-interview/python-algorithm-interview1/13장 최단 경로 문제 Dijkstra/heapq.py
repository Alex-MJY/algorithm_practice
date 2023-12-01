# 파이썬은 기본적으로 최소힙을 지원한다. 
# 최대힙을 사용하려면 마이너스 값으로 집어넣고(-value) 마이너스로 꺼내야 한다.(-heapq.heappop(h))
import heapq

# Ascending Heap Sort
def heapsort(iterable):
    h = []
    result = []
    
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
        
    # 힙엡 삽입된 원소를 차례대로 꺼내어 담기        
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8])
print(result)

