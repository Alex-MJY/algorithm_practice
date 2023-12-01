'''역순으로 저장된 연결 리스트의 숫자를 더하라.'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 자료형 변환 type casting
class Solution:
    # 연결 리스트를 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev
    
    # 연결 리스트를 파이썬 리스트로 변환
    def toList(self, node: ListNode) -> ListNode:
        li: list = []
        while node:
            li.append(node.val)
            node = node.next
        return li
    
    # 파이썬 리스트를 연결 리스트로 변환
    def toReversedLinkedList(self, result: ListNode) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node
        return node
    
    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, list1: ListNode, list2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(list1))
        b = self.toList(self.reverseList(list2))
        
        resultStr = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        
        return self.toReversedLinkedList(str(resultStr))