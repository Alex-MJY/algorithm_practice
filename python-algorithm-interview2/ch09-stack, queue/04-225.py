'''큐를 이용해 다음 연산을 지원하는 스택을 구현하라 : push(), pop(), top(), empty()'''

# 보통 스택이나 큐 ADT를 실제로 구현할 때는, 스택은 연결리스트, 큐는 배열로 한다.
# 파이썬의 리스트나 데크는 스택과 큐의 모든 기능을 제공한다.


# push() 할 때 큐를 이용해 재정렬.
# 요소를 삽입한 후에 방금 삽입한 요소를 맨 앞에 두는 상태로 전체를 재정렬한다.
# 큐에서 맨 앞 요소를 뺄 때, 스택처럼 가장 먼저 삽입한 요소가 나오게 된다.
import collections

class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()