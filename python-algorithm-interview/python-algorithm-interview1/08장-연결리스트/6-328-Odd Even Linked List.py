# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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

'''
공간 복잡도와 시간 복잡도의 제약 사항이 있다. 제약이 없다면 연결 리스트를 리스트로 바꾸고 
슬리이싱과 같은 함수를 사용해서 직관적으로 풀 수 있지만 불가능하다.

홀수 노드 다음에 짝수 노드가 오게 재구성하라고 했으니, odd와 even 노드를 구성한 다음에
홀수 노드의 마지막을 짝수 노드의 처음과 이어주면 된다.

홀수 = odd = head
짝수 = even = head.next
even_head = head.next (홀수와 이어줄 짝수의 head)
'''
