# Definition for singly-linked list.
# class Listcur:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        # cur, rev = head, None
        # while cur:
        #     next, cur.next = cur.next, rev
        #     rev, cur = cur, next
        # return rev
        
        cur = head
        rev = None
        
        while cur:
            next = cur.next
            cur.next = rev
            rev = cur
            cur = next
        return rev
        
'''
이전 값을 rev로 이어주면서 동시에 cur는 앞으로 나가야 되는데 cur.next 값을 rev로 바꿔주기 때문에
next 변수에 cur.next 값을 고정으로 담아서 앞으로 이동할 수 있도록 한다.

rev는 cur의 앞의 값을 가르킨 이후 rev에 cur를 넣어서 진전한다.
'''