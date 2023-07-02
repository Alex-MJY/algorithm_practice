'''원형 큐를 디자인하라'''


# 배열을 이용한 풀이
# 원형 큐는 FIFO 구조를 지닌다는 점에서 기존의 큐와 동일하다. 그러나 마지막 위치가 시작 위치와 연결되는 원형 구조이기 때문에, Ring Buffer라고도 부른다
# 기존의 큐는 공간의 꽉 차면 더 이상 요소를 추가할 수 없는데, 원형큐는 앞쪽에 공간이 남아 있다면 추가할 수 있다.

# enQeue()를 하면 rear 포인터가 앞으로 이동하고, deQeue()를 하면 front 포인터가 앞으로 이동한다. 투 포인터가 돌면서 이동하는 구조가 된다.
# 투 포인터가 같은 위치에서 만나면, 여유 공간이 없다는 의미다.

class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0 # front
        self.p2 = 0 # rear
        
    # enQueue() : move rear pointer
    def enQueue(self, value: int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen # modular 계산으로 포인터의 위치가 전체 길이 벗어나지 않도록 제한
            return True
        else:
            return False
        
    # deQueue() : move front pointer
    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True
        
    def Front(self) -> int:
        # if self.q[self.p1] is None:
        #     return -1
        # else:
        #     return self.q[self.p1]
        return -1 if self.q[self.p1] is None else self.q[self.p1]
    
    def Rear(self) -> int:
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]
    
    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None
    
    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None