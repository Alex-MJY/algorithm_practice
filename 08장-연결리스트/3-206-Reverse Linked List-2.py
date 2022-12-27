# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node, prev = head, None
        # while node:
        #     next, node.next = node.next, prev
        #     prev, node = node, next
        # return prev
        
        curr = head
        prev = None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        
'''
이전 값을 prev로 이어주면서 동시에 curr는 앞으로 나가야 되는데 node.next 값을 prev로 바꿔주기 때문에
next 변수에 node.next 값을 고정으로 담아서 앞으로 이동할 수 있도록 한다.

prev는 curr의 앞의 값을 가르킨 이후 prev에 curr를 넣어서 진전한다.
'''