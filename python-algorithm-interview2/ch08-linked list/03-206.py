'''연결 리스트를 뒤집어라'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
# recursive 
# 다음 노드 next와 현재 노드 node를 파라미터로 지정한 함수를 계속 재귀 호출한다.
# node.next에는 이전 prev 리스트를 계속 연결해주면서 node가 None이 될 때까지 재귀호출하면 마지막에 백트래킹되면서 연결 리스트가 거꾸로 연결된다.
# 맨 처음에 리턴된 prev는 뒤집힌 연결 리스트의 첫 번째 노드가 된다.
class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head, None)
    
# iterative
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev