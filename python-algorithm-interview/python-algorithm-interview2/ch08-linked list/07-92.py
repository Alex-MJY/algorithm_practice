'''인덱스 left에서 right까지를 역순으로 만들어라. 인덱스 m은 1부터 시작한다.'''

# start는 left의 바로 앞 지점을 가리키고, end는 start.next로 지정한다. (할당된 start,end는 끝까지 값이 변하지 않는다)
# root에 맨 앞 값인 head의 이전으로 위치시킨다. root.next를 최종 결과로 리턴하게 될 것이다.
# start.next를 tmp로 지정하고, start.next는 end.next가 된다. 
# 그리고 end.next는 end.next.next로 한 칸 더 앞의 값을 이끌어온다.
# 위의 구조로 (right - left)만큼 반복한다.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int):
        # exception handling
        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head

        # start, end 지정
        for _ in range(left - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(right - left):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp
        return root.next