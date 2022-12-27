# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            #값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return head
    
'''
대개 연결 리스트는 복잡한 여러 가지 값들의 구조체로 구성되어 있기 때문에 값만 교환하는 방법은 실용성은 없다.
그러나 이 문제는 간단한 single linked list이기 때문에 쉽게 풀 수 있다.
'''