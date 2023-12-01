'''연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간복잡도 O(1), 시간복잡도 O(n)에 풀이하라'''

# 반복 구조로 홀짝 노드 처리
# 홀, 짝 각 노드를 구성한 다음 홀수 노드의 마지막을 짝수 노드의 처음와 이어주는 방법
# 홀수 변수는 head이고, 짝수 변수는 head.next이다. 
# 짝수의 헤드는 head.next이므로, even_head = even = head.next로 시작한다.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode):
        # exception handling
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head        