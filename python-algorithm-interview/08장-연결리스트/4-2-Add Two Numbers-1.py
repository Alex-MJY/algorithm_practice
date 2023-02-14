# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # !!! 연결 리스트를 문자열로 이어 붙인 다음에 숫자로 변환하고, 계산한 후 다시 연결 리스트로 바꿔준다.
    
    # 연결리스트 뒤집기
    def reverseList(self, head):
        curr, prev = head, None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    # 연결리스트를 파이썬 리스트로 변환
    def toList(self, node):
        li = []
        while node:
            li.append(node.val)
            node = node.next
        return li
    
    # 파이썬 리스트를 연결리스트로 변환
    def toReverseLinkedList(self, result):
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        result = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        return self.toReverseLinkedList(str(result))