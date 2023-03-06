class BinaryHeap(object):
    def __init__(self):
        self.items = [None]
        
    def __len__(self):
        return len(self.items) - 1
    
    
# Up-Heap, 삽입, percolate_up()
# 1. 요소를 가장 하위 레벨의 최대한 왼쪽으로 삽입한다. (배열로 표현할 경우 가장 마지막에 삽입한다.)
# 2. 부모 값과 비교해 값이 더 작은 경우 위치를 변경한다.
# 3. 계속해서 부모 값과 비교해 위치를 변경한다. (가장 작은 값일 경우 루트까지 올라감)
    def _percolate_up(self): # 내부함수라는 의미로 함수명 앞에 밑줄을 부여했다.
        i = len(self)
        parent = i // 2
        while parent >= 0:
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items = self.items[i], self.items[parent]
            i = parent
            parent = i // 2
            
    def insert(self, k): # 삽입 자체는 insert()를 호출해 실행한다. 시간 복잡도는 O(log n)이다.
        self.items.append(k)
        self._percolate_up() 
        
        
# Down-Heap, 추출은 매우 간단하다. 루트를 추출하면 된다. 추출 이후에 힙의 특성을 유지하는 작업이 필요하기 때문에 시간복잡도는 O(log n)이다.
    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx
        
        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right
            
        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self._percolate_down(smallest)
            
    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted
            
    
'''
Binary Heap VS Binary Search Tree

힙은 상/하 관계를 보장하며, 특히 최소 힙에서는 부모가 항상 자식보다 작다.
반면 BST는 좌/우 관계를 보장한다. 부모는 왼쪽 자식보다는 크며, 오른쪽 자식보다는 작거나 같다.
BST는 탐색과 삽입 모드 O(log n)에 가능하며, 모든 값이 정렬되어야 할 때 사용한다.
반면 가장 큰 값을 추출하거나(최대 힙) 가장 작은 값을 추출(최소 힙)하려면 이진 힙을 사용해야 한다.
이진 힙은 이 작업이 O(1)에 가능하다. 우선순위와 연관되어 있으며 따라서 이진 힙은 우선순위 큐에 활용된다.
'''