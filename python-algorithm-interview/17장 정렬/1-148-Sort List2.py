# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 연결리스트 -> 파이썬리스트
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next

        lst.sort()

        # 파이썬리스트 -> 연결리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head

# 내장 함수 이용