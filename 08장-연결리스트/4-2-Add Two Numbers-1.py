# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 연결리스트 뒤집기
    def reverseList(self, head: ListNode):
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    # 연결리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode):
        li = []
        while node:
            li.append(node.val)
            node = node.next
        return li

    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: ListNode):
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node

    # 두 연결 리스트의 덧셈    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        # 최종 계산 결과 연결 리스트 변환
        return self.toReversedLinkedList(str(resultStr))